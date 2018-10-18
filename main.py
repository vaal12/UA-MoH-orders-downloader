# -*- coding: utf-8 -*-

import requests

#in console run 
#      chcp 65001
#first - to ensure that UTF-8 is properly displayed
#https://stackoverflow.com/questions/3578685/how-to-display-utf-8-in-windows-console


import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


import globals
from utils import getPage
from parsePage import parseNakazPage

import os, codecs

nakaz_counter = 1


new_page_num = "-1"
r = getPage(globals.BASE_PAGE_URL, globals.PAGE_FILES_DIR)
new_page_num = parseNakazPage(r)
print("New page Num:{}".format(new_page_num))
while new_page_num <> "2":
    r = getPage(globals.BASE_PAGE_URL+"page={}".format(new_page_num),
            globals.PAGE_FILES_DIR)
    new_page_num = parseNakazPage(r)
    print("New new page num:{}".format(new_page_num))
