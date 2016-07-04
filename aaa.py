#  coding: utf-8

import sys
import os
import time
import json
import re
import requests
from bs4 import BeautifulSoup

print "好吧"
print json.JSONDecoder, json.JSONEncoder

print os.getcwd()

# json.load()

p = os.getcwd()
# with open() as cf:

p = re.compile("((?<=a)[0-9]+)b")
print p.search("a22bsldfjalja333b").groups()
print p.sub('__', 'a239457bsldfjalja34957b')

print '''
==== sdlfjei ==============='''

url = "http://www.ishadowsocks.com/"
resp = requests.get(url)
# print resp.content, type(resp)

# re.co

# pattern = '''<div class="col-lg-4 text-center">(.*?)</div>'''
pattern = "<section[.\n]*"
# pattern = '<a>.*?</a>'
# regex = re.compile(pattern)
# list = regex.findall(resp.content)
# print list

soup = BeautifulSoup(resp.content, 'html.parser')

serverList = []
for server in soup.select('section#free')[0].select('.row div'):
    print "===============\n" * 2
    serverStr = str(server).strip().replace('\n', '')
    if serverStr.find("服务器地址") < 0:
        continue
    # print serverStr


    serverAddr = re.findall("服务器地址:(.*?)<", serverStr)[0]
    serverPort = re.findall("端口:(.*?)<", serverStr)[0]
    serverPass = re.findall("密码:(.*?)<", serverStr)[0]
    serverEncry = re.findall("加密方式:(.*?)<", serverStr)[0]

    print serverAddr, serverPort, serverPass, serverEncry

    serverObj = {
        "server": serverAddr,
        "server_port": int(serverPort),
        "password": serverPass,
        "method": serverEncry,
        "remarks": serverAddr + " - " + serverPass
    }
    print "---->\n", serverObj
    serverList.append(serverObj)
    print "---->\n", serverList

print "---->\n", serverList[1].get("encrypt")


# update conf file
def updateCf(f, serverInfoList):
    with open(f, 'r+') as cf:
        print cf.name
        cfDict = json.load(cf)
        cfDict['configs'] = serverInfoList
        print cfDict

    with open(f, 'w') as cf:
        json.dump(cfDict, cf, indent=4)


with open('test.json', 'w') as test:
    json.dump({'wat': ['a', 'b']}, test, indent=4)

# print 'cwd: ', os.getcwd()
# with open('gui-config.json', 'r') as file:
#     cf = json.load(file)
#     print cf
#     cf['configs'] = serverList
#     print cf
#
# with open('gui-config.json', 'w+') as file:
#     json.dump(cf, file, indent=4)


    # with open('test.json', 'w+') as dish:
    #     json.dump(cf, dish, indent=4)

cfFile = 'gui-config.json'
updateCf(cfFile, serverList)

print "sleeping... 5s"
time.sleep(5)
print "bye"
