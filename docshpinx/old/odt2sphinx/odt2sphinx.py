# -*- coding: utf-8 -*-
import codecs
import itertools
import os
import re
import sys
import subprocess
import zipfile

try:
    import Image
except ImportError:
    from PIL import Image

from xml.etree import cElementTree as et

import optparse

import six
from six import BytesIO
from six import u
from six.moves import configparser

if not six.PY3:
    def next(i):
        return i.next()

try:
    from os.path import relpath
except ImportError:
    def relpath(path, start):
        """Return a relative version of a path"""
        if not path:
            raise ValueError("no path specified")
        start_list = os.path.abspath(start).split(os.path.sep)
        path_list = os.path.abspath(path).split(os.path.sep)
        # Work out how much of the filepath is shared by start and path.
        i = len(os.path.commonprefix([start_list, path_list]))
        rel_list = [os.path.pardir] * (len(start_list) - i) + path_list[i:]
        if not rel_list:
            return path
        return os.path.join(*rel_list)

usage = """
  %prog [options] filename.odt [targetdir]
  %prog [options] config.cfg

config.cfg content:
  [path/to/the/file.odt]
  targetdir = path/to/the/targetdir\
"""

parser = optparse.OptionParser(usage)
parser.add_option('--debug', dest='debug', action='store_true')
parser.add_option('--download-source-link', dest='download_source_link',
    action='store_true', default=False)


invalid_filename_characters_re = re.compile(
        '[^-\w]')

filenames = set()


def make_filename(text, unique=True):
    fname = text.encode('ascii', 'replace').decode()
    fname = invalid_filename_characters_re.sub('_', fname)
    if unique:
        if fname in filenames:
            for n in itertools.count(1):
                nfname = '%s%s' % (fname, n)
                if nfname not in filenames:
                    fname = nfname
                    break
        filenames.add(fname)
    return fname


class RstFile(object):
    headings = ['=', '-', '~', "^", '"', "'"]

    def __init__(self):
        self.lines = []
        self.images = {}
        self.indents = []
        self.line_started = False

        self.current_index = -1

        self.current = self

    def __repr__(self):
        return '"%s"' % '\\n'.join(self.lines)

    def _addline(self, line):
        # print('RstFile', '_addline', line, self.current_index)
        if self.current_index == -1:
            self.lines.append(line)
        else:
            self.lines.insert(self.current_index, line)
        if self.current_index != -1:
            self.current_index += 1

    def moveto(self, index):
        self.current_index = index

    @property
    def depth(self):
        return len(self.indents)

    def start_line(self, line=''):
        self.current._start_line(line)

    def _start_line(self, line=''):
        if line != '':
            indent = ''.join(self.indents)
            line = indent + line
        self._addline(line)
        self.line_started = True

    def append(self, line='', dostrip=True):
        self.current._append(line, dostrip)

    def _append(self, line='', dostrip=True):
        
        #modif PVR
        if dostrip:
            if line and line[0:4] == '    ':
                line = line.rstrip(' \n')
            else:
                line = line.strip(' \n')
            
        if len(line) and line[0] in ['*',"'"] and line[-1] in ['*',"'"]:
            # print('line##', line)
            line = ' ' + line + ' '
        
        if self.line_started:
            self.lines[-1] += line
            self.line_started = False
            return
        if line != '':
            indent = ''.join(self.indents)
            line = indent + line
        
        # print('addline', line)
        self._addline(line)

    def heading(self, text, depth):
        self.current._heading(text, depth)

    def _heading(self, text, depth):
        self.append(text)
        self.append(self.headings[depth] * len(text))
        self.append()

    def a(self, href, text):
        self.append('`%s <%s>`_' % (text, href))

    def start_bloc(self, indent=4):
        self.current._start_bloc(indent)

    def _start_bloc(self, indent=4):
        self.indents.append(' ' * indent)

    def end_bloc(self):
        self.current._end_bloc()

    def _end_bloc(self):
        self.indents.pop()
        self._addline('')

    def directive(self, name, *args, **kw):
        self.current._directive(name, *args, **kw)

    def _directive(self, name, *args, **kw):
        self.append('.. %s:: %s' % (
            name, ' '.join(args)))
        self.start_bloc()
        for key, value in kw.items():
            self.append(':%s: %s' % (key, value))
        self.append()

    def simpledirective(self, name, *args, **kw):
        self.current._simpledirective(name, *args, **kw)

    def _simpledirective(self, name, *args, **kw):
        self.directive(name, *args, **kw)
        self.end_bloc()

    def add_image(self, fname, fcontent, width=None, height=None):
        self._add_image(fname, fcontent, width, height)

    def _add_image(self, fname, fcontent, width=None, height=None):
        if fname.endswith('.wmf'):
            try:
                stream = BytesIO(fcontent)
                i = Image.open(stream)
                stream = BytesIO()
                i.save(stream, 'PNG')
                fcontent = stream.getvalue()
                fname = fname[:-4] + '.png'
                del i, stream
            except:
                return
        self.images[fname] = dict(
            content=fcontent,
            width=width,
            height=height)
        self.append('|%s|' % fname.replace('.', '_'))

    def start_table_header(self):
        pass

    def end_table_header(self):
        self.current_table.append('separator')

    def insert_rows_spanned_cells(self):
        row = self.current_table[-1]
        if len(self.current_table) > 1:
            for i in range(len(row), len(self.current_table[0])):
                last_line_i = -2
                separators = 0
                if self.current_table[last_line_i] == 'separator':
                    separators = 1
                    last_line_i -= 1
                last_line = self.current_table[last_line_i]
                if last_line[i][2] > 1:
                    row.append((None, last_line[i][1], last_line[i][2] - 1))
                else:
                    break

    def start_row(self):
        self.current_table.append([])
        self.insert_rows_spanned_cells()

    def end_row(self):
        pass

    def start_cell(self, columns_span, rows_span):
        self.current = RstFile()

        row = self.current_table[-1]
        row.append((self.current, columns_span, rows_span))

        for i in range(1, columns_span):
            row.append((None, columns_span - i, rows_span))

        self.insert_rows_spanned_cells()

    def end_cell(self):
        self.current = self

    def start_table(self):
        self.current_table = []

    def end_table(self):
        column_widths = [0] * len(self.current_table[0])
        row_heights = [0] * len(self.current_table)

        rendered_cells = []
        separator_index = -1

        for row_i, row in enumerate(self.current_table):
            rendered_row = []
            if row == 'separator':
                separator_index = row_i - 1
                continue
            for cell_i, cell in enumerate(row):
                if cell[0] is None:
                    rendered_row.append(cell)
                else:
                    rendered_cell = cell \
                                    and cell[0].getvalue().split('\n') \
                                    or []
                    rendered_row.append((rendered_cell, cell[1], cell[2]))

                    column_widths[cell_i] = max(column_widths[cell_i],
                                                * [len(line)
                                                   for line in rendered_cell])
                    row_heights[row_i] = max(row_heights[row_i],
                                             len(rendered_cell))

            rendered_cells.append(rendered_row)

        if separator_index != -1:
            del row_heights[separator_index + 1]

        def h_border(char='-', skip_columns_groups=[], skip_nodes=[]):
            skip_columns = []
            group_last_columns = []
            for group in skip_columns_groups:
                skip_columns.extend(group)
                group_last_columns.append(group[-1])
            if 0 in skip_columns:
                line = '|'
            else:
                line = '+'
            for col_i, colw in enumerate(column_widths):
                if col_i in skip_columns:
                    line += ' ' * (colw + 2)
                    if col_i in group_last_columns:
                        if col_i + 1 in skip_columns \
                                or col_i + 1 == len(column_widths):
                            line += '|'
                        else:
                            line += '+'
                    else:
                        line += ' '
                else:
                    line += char * (colw + 2)
                    if col_i in skip_nodes:
                        line += char
                    else:
                        line += '+'
            return line

        skip_nodes = []
        for i, cell in enumerate(self.current_table[0]):
            if cell[1] > 1:
                skip_nodes.append(i)
        self.append(h_border(skip_nodes=skip_nodes))

        next_border_char = '-'

        for row_i, row in enumerate(rendered_cells):
            for line_i in range(0, row_heights[row_i]):
                line = '| '
                for cell_i, cell in enumerate(row):
                    if cell[0] is not None and len(cell[0]) > line_i:
                        line += cell[0][line_i] \
                            + ' ' * (column_widths[cell_i]
                                     - len(cell[0][line_i]))
                    else:
                        line += ' ' * column_widths[cell_i]
                    if cell[1] == 1:
                        line += ' | '
                    else:
                        line += '   '
                self.append(line)

            skip_columns_groups = [[]]
            for i, cell in enumerate(row):
                if cell[2] > 1:
                    skip_columns_groups[-1].append(i)
                if cell[1] == 1:
                    if skip_columns_groups[-1]:
                        skip_columns_groups.append([])
            if not skip_columns_groups[-1]:
                del skip_columns_groups[-1]

            skip_nodes = []
            for i, cell in enumerate(row):
                next_row_i = row_i + 1
                if cell[1] > 1 and (
                        row_i == len(rendered_cells) - 1
                        or rendered_cells[next_row_i][i][1] > 1):
                    skip_nodes.append(i)

            next_border_char = '-'
            if row_i == separator_index:
                next_border_char = '='
            border = h_border(char=next_border_char,
                              skip_columns_groups=skip_columns_groups,
                              skip_nodes=skip_nodes)
            self.append(border)

        self.append()

    def getvalue(self):
        lines = list(self.lines)

        for fname in self.images.keys():
            width = self.images[fname]['width']
            height = self.images[fname]['height']
            kw = {}
            if width:
                kw['width'] = width
            if height:
                kw['height'] = height
            self.simpledirective('|%s| image' % fname.replace('.', '_'),
                                 'images/' + fname, **kw)

        output = self.lines
        self.lines = lines
        return u('\n').join(output)


class SphinxWriter(object):
    def __init__(self, title, dir, options=None):
        self.dir = dir
        self.bloc_depth = -1

        self.options = options or {}

        self.files = {}

        self.current_file = RstFile()
        self.files['index'] = self.current_file

    def __getattr__(self, name):
        return getattr(self.current_file, name)

    def option(self, name):
        return self.options.get(name, '')

    def bool_option(self, name):
        return self.options.get(name, False)

    def append(self, text, dostrip=True):
        # print('SphinxWriter', 'append', text)
        self.current_file.append(text, dostrip)

    def add_image(self, fname, fcontent, width=None, height=None):
        self.current_file.add_image(fname, fcontent,
                                    width=width, height=height)

    def add_text(self, text, font_style=None):
        # print('SphinxWriter', 'add_text', text, self.current_file.line_started)
        if font_style == 'italic':
            text = '*' + text + '*'
        elif font_style == 'underline':
            text = '*' + text + '*'
        elif font_style == 'bold':
            text = '**' + text + '**'
        elif font_style == 'fixed':
            text = '``' + text + '``'
        # print('add_text', text,'-')
        self.append(text, dostrip=False)

    def h0(self, text):
        self.current_file.heading(text, 0)

    def h1(self, text):
        if self.current_file == self.files['index']:
            self.current_file.directive('toctree', maxdepth=2)
        self.current_file = RstFile()
        fname = make_filename(text)
        self.files[fname] = self.current_file

        self.files['index'].append(fname)

        self.current_file.heading(text, 0)

    def h2(self, text):
        self.current_file.heading(text, 1)

    def h3(self, text):
        self.current_file.heading(text, 2)

    def h4(self, text):
        self.current_file.heading(text, 3)

    def h5(self, text):
        self.current_file.heading(text, 4)

    def h6(self, text):
        self.current_file.heading(text, 5)

    def a(self, href, text):
        self.current_file.a(href, text)

    def p_start(self):
        # print('SphinxWriter', 'p_start')
        #self.current_file.start_bloc()
        pass

    def p_end(self):
        #pvr
        # print('SphinxWriter', 'p_end')
        #self.current_file.end_bloc()
        self.current_file.append()
        
    def span_start(self):
        if len(self.current_file.lines):
            self.current_file.line_started = True
            # print('span_start', self.current_file.lines)
        # print('SphinxWriter', 'span_start')
        
    def span_end(self):
        # print('SphinxWriter', 'span_end')
        pass
        


    def directive(self, *args, **kw):
        self.current_file.directive(*args, **kw)

    def list_item(self, text=None, numbered=False):
        if numbered:
            self.current_file.start_line('#.  ')
        else:
            self.current_file.start_line('*   ')
        if text is not None:
            self.current_file.append(text)
            self.current_file.append()
        else:
            self.current_file.start_bloc(4)

    def end_bloc(self):
        self.current_file.end_bloc()

    def finalise(self):
        if len(self.files) > 1:
            self.files['index'].end_bloc()

    def writeout(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        if not os.path.exists(os.path.join(self.dir, 'images')):
            os.mkdir(os.path.join(self.dir, 'images'))
        for fname, rstfile in self.files.items():
            sys.stdout.write("Generate %s... " % fname)
            fname = os.path.join(self.dir, fname) + '.rst'
            lastcontent = None
            if os.path.exists(fname):
                lastcontent = codecs.open(fname, 'r', 'utf8').read()
            content = rstfile.getvalue()
            if self.bool_option('download_source_link'):
                content += """
.. only:: html

    OpenOffice source: :download:`%s <%s>`.

""" % (os.path.basename(self.option('download_source_link')),
    self.option('download_source_link'))
            if content != lastcontent:
                f = codecs.open(fname, 'w', 'utf8')
                f.write(content)
                f.close()
                print("Done")
            else:
                print("No change")

            if rstfile.images:
                print("Saving images...")
            for fname, attrs in rstfile.images.items():
                fname = os.path.join(self.dir, 'images', fname)
                fcontent = attrs['content']
                lastcontent = None
                if os.path.exists(fname):
                    lastcontent = open(fname, 'rb').read()
                if fcontent != lastcontent:
                    f = open(fname, 'wb')
                    f.write(fcontent)
                    f.close()


class ODTReader(object):
    style_map = {
        'Heading': 'h0',
        'Heading_20_1': 'h1',
        'Heading_20_2': 'h2',
        'Heading_20_3': 'h3',
        'Heading_20_4': 'h4',
    }
    ns = dict(
        office="urn:oasis:names:tc:opendocument:xmlns:office:1.0",
        style="urn:oasis:names:tc:opendocument:xmlns:style:1.0",
        text="urn:oasis:names:tc:opendocument:xmlns:text:1.0",
        table="urn:oasis:names:tc:opendocument:xmlns:table:1.0",
        tableooo="http://openoffice.org/2009/table",
        draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
        fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
        xlink="http://www.w3.org/1999/xlink",
        dc="http://purl.org/dc/elements/1.1/",
        meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0",
        number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
        svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
        chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0",
        dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0",
        math="http://www.w3.org/1998/Math/MathML",
        form="urn:oasis:names:tc:opendocument:xmlns:form:1.0",
        script="urn:oasis:names:tc:opendocument:xmlns:script:1.0",
        ooo="http://openoffice.org/2004/office",
        ooow="http://openoffice.org/2004/writer",
        oooc="http://openoffice.org/2004/calc",
        dom="http://www.w3.org/2001/xml-events",
        xforms="http://www.w3.org/2002/xforms",
        xsd="http://www.w3.org/2001/XMLSchema",
        xsi="http://www.w3.org/2001/XMLSchema-instance",
        rpt="http://openoffice.org/2005/report",
        of="urn:oasis:names:tc:opendocument:xmlns:of:1.2",
        rdfa="http://docs.oasis-open.org/opendocument/meta/rdfa#",
        field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0",
        formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0",
        )

    def __init__(self, filename, visitor, debug=False):
        self.debug = debug
        self.filename = os.path.abspath(filename)
        self.dirname = os.path.dirname(self.filename)
        file = open(filename, 'rb')
        self.archive = zipfile.ZipFile(file)
        self.xml_content = self._load_xml('content.xml')
        self.xml_styles = self._load_xml('styles.xml')
        self.meta = self._load_xml('meta.xml')
        self.visitor = visitor

        self._load_styles()
        self._load_list_styles()

        self.__it = None
        self.done = False
        
        self.text_append = None
        self.isrootnode = False

    def _load_xml(self, fname):
        buffer = self.archive.read(fname)
        root = et.fromstring(buffer)
        if self.debug:
            p = subprocess.Popen(['/usr/bin/xmllint', '--format', '-'],
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            buffer, _ = p.communicate(buffer)
            open(fname, 'w').write(buffer)
        return root

    def _load_list_styles(self):
        self.list_styles = {None: None}
        stylenodes = self.xml_styles.findall(
                './/{%(text)s}list-style' % self.ns)
        stylenodes.extend(
            self.xml_content.findall('.//{%(text)s}list-style' % self.ns))
        for node in stylenodes:
            name = node.get('{%(style)s}name' % self.ns)
            props = {}
            first_child = node[0]
            if first_child.tag == '{%(text)s}list-level-style-number' % self.ns:
                props['numbered'] = True
            elif first_child.tag == '{%(text)s}list-level-style-bullet' % self.ns:
                props['numbered'] = False
            self.list_styles[name] = props

    def _load_styles(self):
        self.styles = {None: None}
        stylenodes = self.xml_styles.findall('.//{%(style)s}style' % self.ns)
        stylenodes.extend(
            self.xml_content.findall('.//{%(style)s}style' % self.ns))

        for node in stylenodes:
            name = node.get('{%(style)s}name' % self.ns)
            style = dict(name=name)
            for aname in ('display-name', 'family', 'parent-style-name',
                          'next-style-name', 'class'):
                style[aname] = node.get('{%(style)s}' % self.ns + aname)

            for child in node.getchildren():
                if child.tag == '{%(style)s}text-properties' % self.ns:
                    font_style = child.get('{%(fo)s}font-style' % self.ns)
                    if font_style == 'italic':
                        style['font-style'] = 'italic'
                    font_weight = child.get('{%(fo)s}font-weight' % self.ns)
                    if font_weight == 'bold':
                        style['font-style'] = 'bold'
                    underline_style = child.get(
                        '{%(style)s}text-underline-style' % self.ns)
                    if underline_style == 'solid':
                        style['font-style'] = 'underline'

            # Special case. We know that the "Source_xx_Text" styles
            # are for source code.
            if name.startswith("Source_") and name.endswith("_Text"):
                style['font-style'] = 'fixed'

            self.styles[name] = style

        self.style_map = dict(self.style_map)
        for key, style in self.styles.items():
            if style is None:
                continue
            display_name = style['display-name'] or style['name']
            h = None
            if display_name.startswith('Heading'):
                h = 0
                if len(display_name) > 7:
                    try:
                        h = int(display_name[8:])
                    except ValueError:
                        h = None
            if display_name == 'Titre':
                h = 0
            if display_name.startswith('Titre '):
                try:
                    h = int(display_name[6:])
                except ValueError:
                    h = None
            if h is not None:
                self.style_map[key] = 'h%s' % h
            if display_name.lower() in ['note', 'information']:
                self.style_map[key] = 'note'
            if display_name.lower() in ['warning', 'avertissement']:
                self.style_map[key] = 'warning'
            if display_name.lower() in ('tip', 'trucs & astuces'):
                self.style_map[key] = 'tip'
        # print(self.style_map)

    def call_visitor(self, trigger, *args, **kw):
        cb = getattr(self.visitor, trigger, None)
        if cb is not None:
            cb(*args, **kw)

    def start_visit(self, kind, *args, **kw):
        triggername = 'on_%s_start' % kind
        self.call_visitor(triggername, *args, **kw)

    def end_visit(self, kind):
        triggername = 'on_%s_end' % kind
        self.call_visitor(triggername)

    def recurse_node(self, node):
        # print('ODTReader', 'recurse_node',node.text, self.isrootnode, self.visitor.writer.xmltype )
        # print('recurse_node', node.tag)
        # case new pararaph : clean text_append and reurn whole line
        if node.tag in ['{%(text)s}p' % self.ns]:
            if self.text_append is not None :
                self.call_visitor('on_text', self.text_append, font_style=None)
                # print(self.visitor.writer.current_file.lines[-2])
                del self.visitor.writer.current_file.lines[-2]
                
            self.text_append = None
        
        font_style = None
        style_name = node.get('{%(text)s}style-name' % self.ns)
        style = self.styles.get(style_name)
        if style:
            font_style = style.get('font-style')
        
        if node.text:
            # case paragraph start with #
            if node.text[0].encode('utf-8') == '#':
                self.text_append = node.text[1:]
            elif self.text_append is not None:
                self.text_append += node.text
            else:
                self.call_visitor('on_text', node.text, font_style=font_style)
        
        # childreturn = ''
        for i, child in enumerate(node.getchildren()):
            self.handle_node(child)
            if child.tail:
                self.visitor.writer.current_file.line_started = True
                self.call_visitor('on_text', child.tail, font_style=font_style)
                if False:
                    #modif PVR
                    #take care indent
                    previousspace = child.get('{%(text)s}c' % self.ns)
                    temptxt = child.tail
                    if  previousspace and int(previousspace)%4 == 0 : 
                        temptxt = ' ' * int(previousspace) + temptxt
                    #case line begining with #
                    if self.text_append is not None:
                        self.text_append += temptxt
                    else:
                        if len(self.visitor.writer.current_file.lines) :
                            self.visitor.writer.current_file.lines[-1] += ' '
                            self.visitor.writer.current_file.line_started = True
                        self.call_visitor('on_text', temptxt, font_style=font_style)
        
            
            

    def get_node_kind(self, node):
        if node is None:
            return
        if node.tag == '{%(text)s}list-item' % self.ns and len(node) > 0:
            node = node[0]
        style_name = node.get('{%(text)s}style-name' % self.ns)
        style = self.styles[style_name]
        if style and style_name not in self.style_map \
                and style['parent-style-name'] in self.style_map:
            style_name = style['parent-style-name']
            style = self.styles[style_name]
        if style_name in self.style_map:
            kind = self.style_map[style_name]
        else:
            kind = 'p'
        return kind

    def get_image_properties(self, node):
        href = node.get('{%(xlink)s}href' % self.ns)
        if href is None:
            return None, None
        type = node.get('{%(xlink)s}type' % self.ns)
        show = node.get('{%(xlink)s}show' % self.ns)
        fname = href.split('/')[-1]
        if href.startswith('./'):
            href = href[2:]
        if href.startswith('../'):
            fcontent = open(
                os.path.join(self.dirname, href[3:]), mode='rb').read()
        else:
            fcontent = self.archive.read(href)
        return fname, fcontent

    def is_list_numbered(self, node):
        style_name = node.get('{%(text)s}style-name' % self.ns)
        style = self.list_styles[style_name]
        if style is None:
            return False
        return style['numbered']

    def handle_node(self, node):
        
        #self.isrootnode = rootnode
        #if rootnode:
        #    self.rootkind = None
        #print('handle_node', node.tag )
        
        if node.tag in [
                '{%(text)s}span' % self.ns,
                '{%(text)s}s' % self.ns]:
                
            if node.get('{%(text)s}c' % self.ns):
                self.start_visit('span')
                spaces = node.get('{%(text)s}c' % self.ns)
                self.call_visitor('on_text', ' ' * int(spaces), font_style=None)
                self.end_visit('span')
                self.visitor.writer.current_file.line_started = True
                return
                
            self.start_visit('span')
            
            if node.get('{%(text)s}c' % self.ns):
                spaces = node.get('{%(text)s}c' % self.ns)
                self.call_visitor('on_text', ' ' * int(spaces), font_style=None)
                self.visitor.writer.current_file.line_started = True
            else:
                self.recurse_node(node)
                
            self.end_visit('span')
            
            
        if node.tag == '{%(draw)s}frame' % self.ns:
            children = node.getchildren()
            if len(children) == 1 \
                    and children[0].tag == '{%(draw)s}image' % self.ns:
                fname, fcontent = self.get_image_properties(children[0])
                if fname is None:
                    return
                width = node.get('{%(svg)s}width' % self.ns)
                height = node.get('{%(svg)s}height' % self.ns)
                self.call_visitor('on_image', fname, fcontent,
                                  width=width, height=height)
            else:
                self.recurse_node(node)

        if node.tag == '{%(draw)s}image' % self.ns:
            fname, fcontent = self.get_image_properties(node)
            if fname is None:
                return
            self.call_visitor('on_image', fname, fcontent)
        if node.tag == '{%(text)s}list' % self.ns:
            headings = node.findall('.//{%(text)s}h' % self.ns)
            if len(headings):
                for h in headings:
                    self.handle_node(h)
            else:
                self.start_visit('list', numbered=self.is_list_numbered(node))
                self.recurse_node(node)
                self.end_visit('list')
        if node.tag == '{%(text)s}list-item' % self.ns:
            kind = self.get_node_kind(node)
            self.start_visit(kind)
            self.start_visit('list_item')
            self.recurse_node(node)
            self.end_visit('list_item')
            self.end_visit(kind)
            
        if node.tag in (
                '{%(text)s}p' % self.ns,
                '{%(text)s}h' % self.ns):

            kind = self.get_node_kind(node)
            self.start_visit(kind)
            self.recurse_node(node)
            self.end_visit(kind)

        if node.tag == '{%(table)s}table' % self.ns:
            self.start_visit('table')
            self.recurse_node(node)
            self.end_visit('table')

        if node.tag == '{%(table)s}table-column' % self.ns:
            self.call_visitor('table_column',
                repeat=int(node.get(
                    '{%(table)s}number-columns-repeated' % self.ns, 1)))

        if node.tag == '{%(table)s}table-header-rows' % self.ns:
            self.start_visit('table_header_rows')
            self.recurse_node(node)
            self.end_visit('table_header_rows')

        if node.tag == '{%(table)s}table-row' % self.ns:
            self.start_visit('table_row')
            self.recurse_node(node)
            self.end_visit('table_row')

        if node.tag == '{%(table)s}table-cell' % self.ns:
            self.start_visit('table_cell',
                columns_span=int(node.get(
                    '{%(table)s}number-columns-spanned' % self.ns, 1)),
                rows_span=int(node.get(
                    '{%(table)s}number-rows-spanned' % self.ns, 1)),
            )
            self.recurse_node(node)
            self.end_visit('table_cell')

        if node.tag == '{%(table)s}covered-table-cell' % self.ns:
            self.call_visitor('covered_table_cell')

        if node.tag == '{%(text)s}a' % self.ns:
            href = node.get('{%(xlink)s}href' % self.ns)
            self.start_visit('a', href)
            self.recurse_node(node)
            self.end_visit('a')

    def iterate(self):
        nodes = self.xml_content.findall(
            '{%(office)s}body/{%(office)s}text/*' % self.ns)

        for i, el in enumerate(nodes):
            self.handle_node(el)
            yield i, len(nodes)

    def dostep(self):
        if self.__it is None:
            self.__it = self.iterate()

        try:
            i, count = next(self.__it)
        except StopIteration:
            self.done = True


class Converter(object):
    def __init__(self, source, targetdir, debug=False, options=None):
        self.options = options or {}

        self.reader = ODTReader(source, self, debug)
        writeroptions = {}
        if self.bool_option('download_source_link'):
            writeroptions['download_source_link'] = relpath(source, targetdir)
        self.writer = SphinxWriter(source, targetdir, options=writeroptions)
        #self.done = False
        self.buffer = None
        self.last_bloc = None
        self.a_href = None

    def option(self, name):
        return self.options.get(name, '')

    def bool_option(self, name):
        return self.options.get(name, False)

    def _start_buffering(self):
        self.buffer = ''

    def _get_buffer(self):
        b = self.buffer
        self.buffer = None
        return b

    def set_last_bloc(self, name=None):
        changed = name != self.last_bloc
        self.last_bloc = name
        return changed

    def hightlight_start(self, name):
        if self.last_bloc == name:
            self.writer.current_file.start_bloc()
        else:
            self.writer.directive(name)
            self.last_bloc = name

    def hightlight_stop(self, name):
        self.writer.end_bloc()

    def on_p_start(self):
        # print('Converter', 'on_p_start')
        self.set_last_bloc()
        self.writer.p_start()

    def on_p_end(self):
        # print('Converter', 'on_p_end')
        self.writer.p_end()
        
    def on_span_start(self):
        # print('Converter', 'on_span_start')
        self.writer.span_start()
        
    def on_span_end(self):
        # print('Converter', 'on_span_end')
        self.writer.span_end()

    def on_a_start(self, href):
        assert self.a_href is None, "Nested anchors are not supported"
        self.a_href = href
        self._start_buffering()

    def on_a_end(self):
        self.writer.a(self.a_href, self._get_buffer())
        self.a_href = None

    def on_note_start(self):
        self.hightlight_start('note')

    def on_note_end(self):
        self.hightlight_stop('note')

    def on_warning_start(self):
        self.hightlight_start('warning')

    def on_warning_end(self):
        self.hightlight_stop('warning')

    def on_tip_start(self):
        self.hightlight_start('tip')

    def on_tip_end(self):
        self.hightlight_stop('tip')

    def on_h0_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h0_end(self):
        self.writer.h0(self._get_buffer())

    def on_h1_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h1_end(self):
        self.writer.h1(self._get_buffer())

    def on_h2_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h2_end(self):
        self.writer.h2(self._get_buffer())

    def on_h3_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h3_end(self):
        self.writer.h3(self._get_buffer())

    def on_h4_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h4_end(self):
        self.writer.h4(self._get_buffer())

    def on_h5_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h5_end(self):
        self.writer.h5(self._get_buffer())

    def on_h6_start(self):
        self.set_last_bloc()
        self._start_buffering()

    def on_h6_end(self):
        self.writer.h6(self._get_buffer())

    def on_list_start(self, numbered):
        # print('Converter', 'on_list_start')
        self.numbered_list = numbered

    def on_list_end(self):
        # print('Converter', 'on_list_end')
        pass

    def on_list_item_start(self):
        self.writer.list_item(numbered=self.numbered_list)

    def on_list_item_end(self):
        self.writer.end_bloc()

    def on_text(self, text, font_style=None):
        # print('add_text', text, self.buffer)
        if self.buffer is not None:
            self.buffer += text
        else:
            #print('add_text', text)
            self.writer.add_text(text, font_style=font_style)

    def on_image(self, fname, fcontent, width=None, height=None):
        if fname.find('.') == -1:
            fname += '.png'
        fname = fname.replace(' ', '_')
        self.writer.add_image(fname, fcontent, width=width, height=height)

    def on_table_start(self):
        self.writer.start_table()

    def on_table_end(self):
        self.writer.end_table()

    def on_table_column(self, repeat=1):
        pass

    def on_table_header_rows_start(self):
        self.writer.start_table_header()

    def on_table_header_rows_end(self):
        self.writer.end_table_header()

    def on_table_row_start(self):
        self.writer.start_row()

    def on_table_row_end(self):
        self.writer.end_row()

    def on_table_cell_start(self, columns_span=1, rows_span=1):
        self.writer.start_cell(columns_span=columns_span, rows_span=rows_span)

    def on_table_cell_end(self):
        self.writer.end_cell()

    def dostep(self):
        self.reader.dostep()
        if self.reader.done:
            self.finalise()

    def finalise(self):
        self.writer.finalise()
        self.writer.writeout()

    @property
    def done(self):
        return self.reader.done


def convert_odt(filename, targetdir, options=None, debug=False):
    converter = Converter(filename, targetdir, debug=debug,
        options=options)

    while not converter.done:
        converter.dostep()


def main():
    options, args = parser.parse_args()
    if len(args) == 1 and args[0].endswith('.odt'):
        args.append(args[0][:-4])
    if len(args) == 2:
        filename, targetdir = args
        convert_odt(filename, targetdir, debug=options.debug,
            options={
                'download_source_link': options.download_source_link
                })
    elif len(args) == 1:
        configname = os.path.abspath(args[0])
        configdir = os.path.dirname(configname)
        config = configparser.ConfigParser()
        config.read(configname)
        for section in config.sections():
            filename = config.has_option(section, 'filename') and \
                config.get(section, 'filename') or section
            filename = os.path.normpath(
                os.path.join(configdir, filename))
            targetdir = config.has_option(section, 'targetdir') and \
                config.get(section, 'targetdir') or '.'
            targetdir = os.path.normpath(
                os.path.join(configdir, targetdir))
            print("Converting %s in %s" % (filename, targetdir))
            convert_odt(filename, targetdir, debug=options.debug,
                options={'download_source_link': options.download_source_link})

if __name__ == '__main__':
    main()
