PAGE_FILES_DIR = "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\"
#RESULT_FILES_DIR = "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\DOWNLOADED_FILES\\"

RESULT_FILES_DIR = "c:\\MOZ\\"

MOZ_BASE_URL = "http://moz.gov.ua/"

BASE_PAGE_URL = "http://moz.gov.ua/nakazi-moz?"

nakaz_counter = 1

INTER_DOWNLOAD_SLEEP = 1  

DIR_NAME_LEN = 60

HTML_PREAMBULE ='''
<html>
 <head>
  <meta charset="UTF-8">
  <title> qwe1 </title>
 </head> 

<body>
'''

HTML_AFTERAMBLE = '''
    </body>
'''

NAKAZY_FILE_TO_WRITE = None