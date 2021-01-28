from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests', views.tests, name='tests'),
    path('validate', views.validate, name='validate'),
    path('add_product', views.add_product, name='add_product'),
    path('product_info', views.product_info, name='product_info'),

]
