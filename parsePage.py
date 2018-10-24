# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import logging, os, codecs

from globals import RESULT_FILES_DIR, nakaz_counter, MOZ_BASE_URL
from globals import INTER_DOWNLOAD_SLEEP, DIR_NAME_LEN
from utils import getPage, downloadFile

def parseNakazPage(page_html):
    soup = BeautifulSoup(page_html)

    legislation_div = soup.find("div", class_="legislation")
    global nakaz_counter
    nakaz_list = legislation_div.find_all("ul")
    for nakazTag in nakaz_list[0].find_all("li"):
        nakaz_link = nakazTag.find("a")
        # print("Link:{}".format(nakaz_link.get("href")))
        # print((u"Text:{}".format("qwe1")).encode("utf-8"))
        nakaz_name = unicode(nakaz_link.get_text()).strip()
        nakaz_name = nakaz_name.replace("\"", "_")
	    nakaz_name = nakaz_name.replace("/", "_")
        logging.debug(nakaz_name)
        nakaz_name = nakaz_name.replace(u"Наказ МОЗ України", "N_M_U")
        dir_name_short = nakaz_name[:DIR_NAME_LEN]+""
        full_dir_name = u"{}{:04d}. {}\\".format(RESULT_FILES_DIR, nakaz_counter, dir_name_short.strip())
        if not os.path.exists(full_dir_name):
            os.mkdir(full_dir_name)

        logging.debug(full_dir_name+"\\info.txt")

        nakaz_actual_link = MOZ_BASE_URL+nakaz_link.get("href")[1:]
        logging.debug(nakaz_actual_link)

        f = codecs.open(full_dir_name+"info.txt", "w", "utf-8")
        f.write(u'\ufeff')
        f.write("Name:\n"+unicode(nakaz_link.get_text()).strip()+"\n\n")
        f.write("URL:\n"+nakaz_actual_link+"\n\n")


        nakaz_content = getPage(nakaz_actual_link, full_dir_name,
            time_to_sleep_before_network=INTER_DOWNLOAD_SLEEP)
        

        #Getting links
        nakaz_soup = BeautifulSoup(nakaz_content)
        f.write("Text:\n")
        # print (nakaz_soup.select("div.editor"))
        for string in nakaz_soup.select("div.editor")[0].stripped_strings:
            # print(repr(string))
            f.write(string)
        f.close()

        

        down_links = nakaz_soup.select("a.download__link")
        for link_tag in down_links:
            print("Have download link:{}".format(link_tag.get("href")))
            descr_tag = link_tag.div
            print("Descr:{}".format(descr_tag.text.encode("utf-8")))

            print("Downloading...")
            downloadFile(MOZ_BASE_URL+link_tag.get("href"), full_dir_name,
                time_to_sleep_before_network=INTER_DOWNLOAD_SLEEP)

        nakaz_counter +=1

    next_page_link = nakaz_list[1].select("li.pagination__arrow_next a")
    print("{}".format(next_page_link[0].get("href")))

    return next_page_link[0].get("href")[17:]