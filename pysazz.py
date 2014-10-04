#!/usr/bin/python
import xml.etree.ElementTree as ET
import urllib.request as urllib
import os
import sys
import sass

config = "pysazz.config.xml"

def init():
    file = open(config, "w")
    file.write("<?xml version=\"1.0\"?>\n<config>\n\t<links>\n\t\t<link folder=\"\">http://mtechnologies.site.nfoservers.com/_file3.scss</link>\n\t</links>\n</config>")
    file.close()

def compile():
    #begin XML parse
    tree = ET.parse(config)
    root = tree.getroot()
                
    #create primary scss file
    file = open("style.scss", "w")

    #download and write imports for all scss files
    for x in range(0, len(root)):
        if root[x].tag == "links":
            for y in range(0, len(root[x])):
                #gets array of attributes and puts files in appropriate directories
                if len(root[x][y].attrib) > 0:
                    if 'folder' in root[x][y].attrib:
                        try:
                            os.stat(root[x][y].attrib['folder'])
                        except:
                            os.makedirs(root[x][y].attrib['folder'])
                    if root[x][y].text[:4] == "http":
                        urllib.urlretrieve (root[x][y].text, root[x][y].attrib["folder"] + "/" + root[x][y].text.split('/')[-1])
                    if root[x][y].text.split('/')[-1][-4:] == "scss" or root[x][y].text.split('/')[-1][-4:] == "sass":
                        file.write("@import \"" + root[x][y].attrib["folder"] + "/" + root[x][y].text.split('/')[-1] + "\";\n")
                #grabs all other files and drops them in the main directory
                else:
                    urllib.urlretrieve (root[x][y].text, root[x][y].text.split('/')[-1])
    #close main scss file
    file.close()

    #compile style.scss
    if len(sys.argv) <= 2:
        compiledString = sass.compile(filename="style.scss")
    else:
        for x in range(0, len(sys.argv)):
            if sys.argv[x][:1] == "-":
                compiledString = sass.compile(filename="style.scss", output_style=sys.argv[x].strip('-'))

    #write compiled sass to file
    outputFile = open("style.css", "w")
    outputFile.write(compiledString)
    outputFile.close()

if sys.argv[1] == "init":
    init()
elif sys.argv[1] == "compile":
    compile()
else:
    print ("Invalid, type sasspy help for more information")