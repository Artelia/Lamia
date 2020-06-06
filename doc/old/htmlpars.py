import lxml
from html.parser import HTMLParser
import os

if False:
    print(os.path.dirname(__file__))
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docs', 'index.html')
    fpath = 'index.html'
    print('ppp', fpath)
    et = xml.etree.ElementTree.parse(fpath)

    a = tree.find('head')
    for b in a.findall('child'):
        print(b)



if False:
    class MyHTMLParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
            print("Encountered a start tag:", tag)

            if tag == 'link':
                #print('okok', attrs)
                if ('rel', 'stylesheet') in attrs:
                    print('pppp', attrs)
                    

        def handle_endtag(self, tag):
            pass
            #print("Encountered an end tag :", tag)

        def handle_data(self, data):
            pass
            #print("Encountered some data  :", data)


    fp = open(os.path.join(os.path.dirname(__file__),'..','docs', 'index.html'))
    lines = fp.readlines()
    parser = MyHTMLParser()
    for line in lines[0:40]:
        parser.feed(line)
            
            
            