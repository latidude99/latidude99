from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owid', views.owid, name='owid'),
    path('covid', views.coviduk, name='coviduk'),
    path('soon', views.soon, name='soon'),

]
