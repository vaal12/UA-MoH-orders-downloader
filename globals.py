PAGE_FILES_DIR = "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\"
#RESULT_FILES_DIR = "c:\\Dev\\04. Python\\05. MOZ nakaz downloader\\DOWNLOADED_FILES\\"

RESULT_FILES_DIR = "c:\\MOZ\\"

MOZ_BASE_URL = "http://moz.gov.ua/"

BASE_PAGE_URL = "http://moz.gov.ua/nakazi-moz?"

nakaz_counter = 1

INTER_DOWNLOAD_SLEEP = 20  

DIR_NAME_LEN = 60

HTML_PREAMBULE ='''
<html>
    <head>
        <meta charset="UTF-8">
        <script type="text/javascript" src="jquery-3.3.1.min.js"></script>
        <script type="text/javascript" src="custom.js"></script>
        <title> qwe1 </title>
    </head> 
    <body>

    <a href="#" id="expandAllLink"> Expand All </a> <br>



'''

HTML_AFTERAMBLE = '''
    
    </body>
</html>
'''

NAKAZY_FILE_TO_WRITE = None