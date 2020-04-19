import csv
import json
import xmltodict
import pprint
import shutil
import os


from htmlgenerator import readDistHtml, parseHtml

SPLIT = ';'
SPLIT_LINE = '<LINE_END>'
# FILENAME = './data/test.csv'
FILENAME = './data/test_2.xml'
DESTINATION = './export/'

def findWEObjects(we, csv_reader_object):
    items = []

    for row in csv_reader_object:
        if(row['WE_'] == we):
            items.append(row)
    return items

def loadObjectsByWEs(weItems, csv_reader_object):
    items = []

    for weId in weItems:
        weobjects = findWEObjects(weId, csv_reader_object)
        items.append(weobjects)
        
    return items

def writeFile(path, filename, html):
    if not os.path.exists(path):
        os.mkdir(path)

    f = open(path + filename, "w")
    f.write(html)
    f.close()


def loadWE_IDS(elements):
    weNumbers = set()
    for row in elements:
        weNumbers.add(row['WE_'])
    return weNumbers

def main():
    pp = pprint.PrettyPrinter(indent=4)

    f = open(FILENAME, "r")
    xmlstring = f.read()

    entries = xmltodict.parse(xmlstring)
    elements = entries['dataroot']['abf900_DataALL']

    weIds = loadWE_IDS(elements)
    mappedElements = loadObjectsByWEs(weIds, elements)


    # Creates RootFile
    html = readDistHtml()
    htmlRootPage = parseHtml(html,"true", list(weIds))

    writeFile(DESTINATION + "root/" , "index.html", htmlRootPage)

    for element in mappedElements:
        htmlobject = parseHtml(html,"false", element)
        pp.pprint(element)

        folder = DESTINATION +  "/" + element[0]['WE_'] +  "/"
        writeFile(folder , "index.html", htmlobject)



if __name__ == "__main__":
    main()
    pass