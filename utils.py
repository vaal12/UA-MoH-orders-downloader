# -*- coding: utf-8 -*-
import requests

import codecs

import os, os.path

import hashlib, time

import logging

def getPage(page_url, BASE_PATH):
    logging.debug("Page URL:{}".format(page_url))
    print(page_url)
    
    file_to_save = BASE_PATH+  \
                        page_url.replace("/", "_").replace("?", "_").replace(":", "_")[:50]+ \
                        "_"+hashlib.sha224(page_url).hexdigest()+ \
                        ".html"
    logging.debug("File name:{}".format(file_to_save.encode("utf-8")))
    if os.path.exists(file_to_save):
        logging.debug("File exists returning from disk")
        f=codecs.open(file_to_save, "r")
        r = f.read()
        f.close()
        return r

    logging.debug("File does not exist: downloading")
    print("File does not exist: downloading")
    time.sleep(10)
    print("Sleep over")
    r = requests.get(page_url)
    #https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python
    f = codecs.open(file_to_save, "w", "utf-8")
    f.write(r.text)
    f.close()
    return r.text