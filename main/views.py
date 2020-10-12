from smtplib import SMTPException

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from main.text import *
import main.service_main as serv
from datetime import datetime as dt
import pytz
from .models import Message



def soon(request):
    context = serv.get_main_ctx()
    return render(request, 'main/soon.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        date = dt.now(pytz.timezone('Europe/London'))
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip = request.environ['REMOTE_ADDR']
        else:
            ip = request.environ['HTTP_X_FORWARDED_FOR']
        app_name = 'main_contact'
        msg = Message(name=name, email=email, subject=subject, message=message, date=date, app_name=app_name, ip=ip)
        try:
            msg.save(using='main')
            serv.send_main_contact_message(msg)
            sent = True
        except SMTPException as e:
            print('There was an error sending an email: ', e)
     #       return render(request, 'main/contact.html', {'error_message': "Ooops, an error occurred while savin the message.",})
        return HttpResponseRedirect(reverse('main:contact_after'))
    else:
        context = serv.get_contact_ctx()
        return render(request, 'main/contact.html', context)


def contact_after(request):
   context = serv.get_contact_after_ctx()
   return render(request, 'main/contact_after.html', context)

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











