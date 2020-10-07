from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soon', views.soon, name='soon'),
    path('covid', views.coviduk, name='coviduk'),
    path('owid', views.owid, name='owid'),
    path('enquiry', views.enquiry, name='enquiry'),

]
