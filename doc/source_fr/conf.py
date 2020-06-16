# -*- coding: utf-8 -*-
#
# inspec documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 02 13:42:07 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
pathsrc = os.path.abspath('../../')
print(pathsrc)
sys.path.insert(0, pathsrc)
path = os.path.abspath('C://OSGeo4W64//apps//qgis//python')
print(path)
sys.path.insert(0, path)

devdocpath = os.path.abspath('..')
sys.path.insert(0, devdocpath)
print(devdocpath)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.napoleon', 
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode'
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates']


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'LAMIA'
copyright = u'2020, Artelia'
author = u'PVR'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Not alphabetycal ordrer
autodoc_member_order = 'bysource'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_logo = "../_static/icon.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_show_sourcelink = False
html_copy_source = False
html_theme_options = {
    'canonical_url': '',
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # 'vcs_pageview_mode': '',
    'style_nav_header_background': '#004F83',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    # 'github_banner': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

html_context = {
    # 'source_url_prefix': "https://gitlab.com/anarcat/foo/blob/HEAD/doc/",
    # "display_github": True,
    # "github_host": "gitlab.com",
    # "github_user": "anarcat",
    # "github_repo": 'foo',
    # "github_version": "HEAD",
    # "conf_py_path": "/doc/",
    # "source_suffix": '.rst',
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Mock ------------------------------------------
#autodoc_mock_imports = ["qgis","Lamia.dialog"]
autodoc_mock_imports = ["qgis", "numpy", "pprint","pyspatialite","psycopg2","sqlite3","glob", "collections",
                        "PyQt.QtCore", "PIL", "logging", "xlrd", "math", "re", "os", "sys", "shutils",
                        "pandas" ]


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'inspecdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'inspec.tex', u'inspec Documentation',
     u'PVr', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'inspec', u'inspec Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Inspection digue', u'inspec Documentation',
     author, 'inspec', 'One line description of project.',
     'Miscellaneous'),
]



def setup(app):
    # app.add_stylesheet('theme_overrides.css')
    app.add_css_file('theme_overrides.css')



