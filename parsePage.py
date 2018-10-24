# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import logging, os, codecs, hashlib

import globals 
from utils import getPage, downloadFile

def parseAndDownloadNakaz(nakaz_dir, nakazURL, nakazName):
    f = codecs.open(nakaz_dir+"info.txt", "w", "utf-8")
    f.write(u'\ufeff')
    f.write("Name:\n"+nakazName+"\n\n")
    f.write("URL:\n"+nakazURL+"\n\n")

    globals.NAKAZY_FILE_TO_WRITE.write(
        "MOZ site URL:{} <br>".format(nakazURL)
    )

    #     {}).format(
    #                     unicode(full_dir_name, nakaz_link.get_text()).strip()
    #     )
    # )
    nakaz_content = getPage(nakazURL, nakaz_dir,
        time_to_sleep_before_network=globals.INTER_DOWNLOAD_SLEEP)
    

    #Getting links
    nakaz_soup = BeautifulSoup(nakaz_content)
    f.write("Text:\n")
    # print (nakaz_soup.select("div.editor"))
    body_text = ""
    for string in nakaz_soup.select("div.editor")[0].stripped_strings:
        # print(repr(string))
        body_text += string
        f.write(string)
    f.close()

    globals.NAKAZY_FILE_TO_WRITE.write(
        u"Text:{} <br>".format(body_text)
    )

    down_links = nakaz_soup.select("a.download__link")
    for link_tag in down_links:
        print("Have download link:{}".format(link_tag.get("href")))
        descr_tag = link_tag.div
        print("Descr:{}".format(descr_tag.text.encode("utf-8")))

        print("Downloading...")
        downloadFile(globals.MOZ_BASE_URL+link_tag.get("href"), nakaz_dir,
            time_to_sleep_before_network=globals.INTER_DOWNLOAD_SLEEP)
#END def parseAndDownloadNakaz(nakaz_dir, nakazURL, nakazName):

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
        full_dir_name = globals.RESULT_FILES_DIR+dir_name_short

        nakaz_name_for_HTML = nakaz_link.get_text().strip().replace("\"", "&quot;")

        # print(globals.NAKAZY_FILE_TO_WRITE)
        globals.NAKAZY_FILE_TO_WRITE.write(
            u"<a href=\"file://{}\"> {:04d}.{} </a><br>\n\n".format(
                full_dir_name,
                globals.nakaz_counter,
                nakaz_name_for_HTML
            )
        )
        # globals.NAKAZY_FILE_TO_WRITE.write(
        #     nakaz_name_for_HTML) 
        # globals.NAKAZY_FILE_TO_WRITE.write(
        #     "   ")

        
        if not os.path.exists(full_dir_name):
            logging.debug(full_dir_name+"\\info.txt")
            os.mkdir(full_dir_name)
            parseAndDownloadNakaz(full_dir_name, nakaz_actual_link,
                    nakaz_name)
            
        #END: if not os.path.exists(full_dir_name):
        else: print("Not downloading nakaz")

        globals.nakaz_counter +=1

    next_page_link = nakaz_list[1].select("li.pagination__arrow_next a")
    print("{}".format(next_page_link[0].get("href")))

    return next_page_link[0].get("href")[17:]

#END def parseNakazPage(page_html):