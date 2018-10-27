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

import os, codecs, datetime




#https://www.tutorialspoint.com/python/time_strftime.htm
f = codecs.open("nakazy_{}.html".format(datetime.datetime.now().strftime("%d-%b-%Y")), 
            "w", "utf-8")
f.write(globals.HTML_PREAMBULE)
f.write(datetime.datetime.now().strftime("%d:%m:%Y %H:%M"))
f.write("\n\n<br><br>")
globals.NAKAZY_FILE_TO_WRITE = f
# print(globals.NAKAZY_FILE_TO_WRITE)

new_page_num = "-1"
r = getPage(globals.BASE_PAGE_URL, globals.PAGE_FILES_DIR)
new_page_num = int(parseNakazPage(r))
print("New page Num:{}".format(new_page_num))
while new_page_num <= globals.PAGE_NUMBER_TO_STOP_AT:
    r = getPage(globals.BASE_PAGE_URL+"page={}".format(new_page_num),
            globals.PAGE_FILES_DIR)
    new_page_num = int(parseNakazPage(r))
    print("New new page num:{}".format(new_page_num))

globals.NAKAZY_FILE_TO_WRITE.write(globals.HTML_AFTERAMBLE)
globals.NAKAZY_FILE_TO_WRITE.close()

# os.system("c:\Portables\GoogleChromePortable\GoogleChromePortable.exe nakazy.html")
