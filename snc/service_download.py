#import django
#django.setup()

import mechanicalsoup

from snc.const import *
import untangle
import datetime as dt
import time


def download_catalogue_and_check(u,p):
    try:
        download_catalogue(u, p)
        time.sleep(5)
        check = check_catalogue_file()
    except:
        status = '---'
        check = [status]
    return check



def download_catalogue(username, password):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL_UKHO_LOGIN)
    browser.select_form()  # ('form[action="/Login?again=1"]')
    browser.get_current_form().print_summary()
    browser["username"] = username
    browser["password"] = password
    response = browser.submit_selected()
    browser.open(URL_UKHO_DOWNLOAD)
    a = browser.get_current_page().find('a', id='MDSPages_linkDlPaperXml')
    file_url = URL_UKHO_BASE + a['href']
    print(file_url)
    browser.download_link(link=a, file=SNC_CATALOGUE_FILE)
    print('Catalogue downloaded successfully')


def check_catalogue_file():
    try:
        obj = untangle.parse(SNC_CATALOGUE_FILE)
        meta = obj.UKHOCatalogueFile.BaseFileMetadata
        catalogue_number = meta.MD_FileIdentifier.cdata
        catalogue_date = dt.datetime.strptime(meta.MD_DateStamp.cdata, '%Y-%m-%d').date()
        catalogue_lines = file_len(SNC_CATALOGUE_FILE)
        status = 'ok'
        check = [status, catalogue_number, catalogue_date, catalogue_lines]
    except:
        status = '---'
        check = [status]

    return check


def file_len(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



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













