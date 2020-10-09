from django.shortcuts import render
from django.http import HttpResponse
from main.text import *
import main.service_main as serv



def soon(request):
    context = serv.get_main_ctx()
    return render(request, 'main/soon.html', context)

def contact(request):
    context = serv.get_contact_ctx()
    return render(request, 'main/contact.html', context)

def index(request):
    context = serv.get_index_ctx()
    return render(request, 'main/index.html', context)


def coviduk(request):
    context = serv.get_main_coviduk_ctx()
    return render(request, 'main/coviduk.html', context)


def owid(request):
    context = serv.get_main_owid_ctx()
    return render(request, 'main/owid.html', context)


def enquiry(request):
    context = serv.get_main_enquiry_ctx()
    return render(request, 'main/enquiry.html', context)


def contacts(request):
    context = serv.get_main_contacts_ctx()
    return render(request, 'main/contacts.html', context)


def links(request):
    context = serv.get_main_links_ctx()
    return render(request, 'main/links.html', context)



def maptools(request):
    context = serv.get_main_maptools_ctx()
    return render(request, 'main/maptools.html', context)



def sncreader(request):
    context = serv.get_main_sncreader_ctx()
    return render(request, 'main/sncreader.html', context)



def folderbackup(request):
    context = serv.get_main_folderbackup_ctx()
    return render(request, 'main/folderbackup.html', context)



def maptoolsapp(request):
    context = serv.get_main_maptoolsapp_ctx()
    return render(request, 'main/maptoolsapp.html', context)











