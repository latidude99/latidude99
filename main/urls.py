from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('soon', views.soon, name='soon'),
    path('covid', views.coviduk, name='coviduk'),
    path('owid', views.owid, name='owid'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('contacts', views.contacts, name='contacts'),
    path('links', views.links, name='links'),
    path('maptools', views.maptools, name='maptools'),
    path('maptoolsapp', views.maptoolsapp, name='maptoolsapp'),
    path('sncreader', views.sncreader, name='sncreader'),
    path('folderbackup', views.folderbackup, name='folderbackup'),

]
