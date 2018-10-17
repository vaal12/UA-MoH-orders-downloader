# -*- coding: utf-8 -*-

import requests

#in console run 
#      chcp 65001
#first - to ensure that UTF-8 is properly displayed
#https://stackoverflow.com/questions/3578685/how-to-display-utf-8-in-windows-console

# r = requests.get('http://moz.gov.ua/nakazi-moz')


import codecs

# print(r.encoding)

#https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python
# f = codecs.open("content.html", "w", "utf-8")
# f.write(r.text)
# f.close()


f=codecs.open("content.html", "r")
r = f.read()


from bs4 import BeautifulSoup


import os, os.path

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


soup = BeautifulSoup(r)

# print("soup {}".format(soup))
print("len:{}".format(soup.find_all("div", class_="legislation")))
legislation_div = soup.find("div", class_="legislation")
nakaz_counter = 1
path_to_dirs = "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\"
nakaz_list = legislation_div.find_all("ul")
for nakazTag in nakaz_list[0].find_all("li"):
    # print(nakazTag.string)
    nakaz_link = nakazTag.find("a")
    print("Link:{}".format(nakaz_link.get("href")))
    print((u"Text:{}".format("qwe1")).encode("utf-8"))
    nakaz_name = unicode(nakaz_link.get_text()).strip()
    # print((u"ля ля ля").encode("utf-8"))
    nakaz_name = nakaz_name.replace("\"", "_")
    logging.debug(nakaz_name)
    logging.debug("c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\"+nakaz_name)
    # dir_name = u"c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\"+nakaz_name
    logging.debug(nakaz_name)
    dir_name_short = nakaz_name[:100]+" ..."
    full_dir_name = u"{}{:04d}. {}".format(path_to_dirs, nakaz_counter, dir_name_short)
    if not os.path.exists(full_dir_name):
        os.mkdir(full_dir_name)
    nakaz_counter +=1



next_page_link = nakaz_list[1].select("li.pagination__arrow_next a")
print("{}".format(next_page_link[0].get("href")))
