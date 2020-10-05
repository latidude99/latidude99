from django.shortcuts import render
from django.http import HttpResponse
from main.text import *
import main.service_main as serv



def index(request):
    context = serv.get_main_index_ctx()
    return render(request, 'main/index.html', context)

def soon(request):
    context = serv.get_main_soon_ctx()
    return render(request, 'main/soon.html', context)

def owid(request):
    context = serv.get_main_owid_ctx()
    return render(request, 'main/owid.html', context)


def coviduk(request):
    context = serv.get_main_coviduk_ctx()
    return render(request, 'main/coviduk.html', context)
