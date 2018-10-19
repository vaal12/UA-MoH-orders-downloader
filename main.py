# -*- coding: utf-8 -*-

import requests

#in console run 
#      chcp 65001
#first - to ensure that UTF-8 is properly displayed
#https://stackoverflow.com/questions/3578685/how-to-display-utf-8-in-windows-console


import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


import globals
from utils import getPage, downloadFile
from parsePage import parseNakazPage

import os, codecs




new_page_num = "-1"
r = getPage(globals.BASE_PAGE_URL, globals.PAGE_FILES_DIR)
new_page_num = parseNakazPage(r)
print("New page Num:{}".format(new_page_num))
while new_page_num <> "2":
    r = getPage(globals.BASE_PAGE_URL+"page={}".format(new_page_num),
            globals.PAGE_FILES_DIR)
    new_page_num = parseNakazPage(r)
    print("New new page num:{}".format(new_page_num))


downloadFile(globals.MOZ_BASE_URL+"uploads/1/7694-dn_20181010_1840.pdf", 
    "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\" 
    )