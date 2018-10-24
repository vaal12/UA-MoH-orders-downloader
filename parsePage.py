# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import logging, os, codecs, hashlib

import globals 
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
        # nakaz_name = nakaz_name.replace(u"Наказ МОЗ України", "N_M_U")
        

        

        nakaz_actual_link = globals.MOZ_BASE_URL+nakaz_link.get("href")[1:]
        logging.debug(nakaz_actual_link)

        # dir_name_short = nakaz_name[:DIR_NAME_LEN]+""
        dir_name_short = hashlib.sha224(nakaz_actual_link).hexdigest()+"\\"
        # full_dir_name = u"{}{:04d}. {}\\".format(RESULT_FILES_DIR, nakaz_counter, dir_name_short.strip())
        full_dir_name = globals.RESULT_FILES_DIR+dir_name_short+"\\"

        nakaz_name_for_HTML = nakaz_link.get_text().strip().replace("\"", "&quot;")

        # print(globals.NAKAZY_FILE_TO_WRITE)
        globals.NAKAZY_FILE_TO_WRITE.write(
            u"<a href=\"file://{}\">".format(full_dir_name))
        globals.NAKAZY_FILE_TO_WRITE.write(
            nakaz_name_for_HTML) 
        globals.NAKAZY_FILE_TO_WRITE.write(
            "   </a><br>\n\n")

        if not os.path.exists(full_dir_name):
            os.mkdir(full_dir_name)



            logging.debug(full_dir_name+"\\info.txt")

            f = codecs.open(full_dir_name+"info.txt", "w", "utf-8")
            f.write(u'\ufeff')
            f.write("Name:\n"+unicode(nakaz_link.get_text()).strip()+"\n\n")
            f.write("URL:\n"+nakaz_actual_link+"\n\n")

            #     {}).format(
            #                     unicode(full_dir_name, nakaz_link.get_text()).strip()
            #     )
            # )
            nakaz_content = getPage(nakaz_actual_link, full_dir_name,
                time_to_sleep_before_network=globals.INTER_DOWNLOAD_SLEEP)
            

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
                downloadFile(globals.MOZ_BASE_URL+link_tag.get("href"), full_dir_name,
                    time_to_sleep_before_network=globals.INTER_DOWNLOAD_SLEEP)
        #END: if not os.path.exists(full_dir_name):
        else: print("Not downloading nakaz")

        globals.nakaz_counter +=1

    next_page_link = nakaz_list[1].select("li.pagination__arrow_next a")
    print("{}".format(next_page_link[0].get("href")))

    return next_page_link[0].get("href")[17:]