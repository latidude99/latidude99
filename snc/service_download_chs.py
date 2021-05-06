import django
django.setup()

import mechanicalsoup

from snc.const import *
import untangle
import datetime as dt
import time
#import wget
import requests


def download_catalogue_and_check(u,p):
    try:
        download_catalogue(u, p)
        time.sleep(5)
        check = check_catalogue_file()
    except:
        status = '---'
        check = [status]
    return check



def download_catalogue():
    file_url = URL_CHS_GEOJSON
    #wget.download(file_url, CHS_GEOJSON_FILE)
    r = requests.get(file_url)
    with open(CHS_GEOJSON_FILE, 'wb') as f:
        f.write(r.content)
    print('Catalogue downloaded successfully')


def file_len(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


download_catalogue()
#check_catalogue_file()






'''
URL downloadPageUrl = new URL(downloadPageString);
Document doc = Jsoup.parse(downloadPageUrl, 5000);
link = doc.getElementById("MDSPages_linkDlPaperXml");
url = link.attr("href");

<a id="MDSPages_linkDlPaperXml" href="Download?file=8815">snc_catalogue.xml [18.93 MB]</a>
https://enavigator.ukho.gov.uk/Download?file=8815
<a href="Download?file=8815" id="MDSPages_linkDlPaperXml">snc_catalogue.xml [18.93 MB]</a>


r = requests.get(file_url)  # create HTTP response object
with open(SNC_CATALOGUE_FILE, 'wb') as f:
   f.write(r.content)
'''













