import shutil
import pprint
import json

TARGET = "./export/dist"


def copyDist():
    try:
        shutil.rmtree(TARGET)
    except:
        print("INFO: Allready removed")
    shutil.copytree( "../swisscom-building-dashboard/dist",TARGET)
    print("INFO: dist copied")


def replaceBetween(original, value ,str1, str2):
    splits = original.split(str1)
    
    first = splits[0]
    last = splits[1].split(str2)[1]

    return first + str1 + value + str2 + last

def generateJSInit(rootPage, jsonString):
    return  "window.ROOT_PAGE = " +rootPage + ";" + \
            "window.GENERATED_DATA = "  + jsonString + ";"

def parseHtml(html, rootPage, obj):
    jsonString  = json.dumps(obj, indent=4, sort_keys=True)

    js = generateJSInit(rootPage, jsonString)
    result = replaceBetween(html, js,'const XXXXXXXXXXXXXXXXXXXXXXXXXXXXX = "X";' , 'const YYYYYYYYYYYYYYYYYYYYYYYYYYYY = "Y";')
    return result\
            .replace("js/", "../dist/js/")\
            .replace("css/", "../dist/css/")

def readDistHtml():
    copyDist()
    f = open(TARGET + "/index.html", "r")
    return f.read()
     