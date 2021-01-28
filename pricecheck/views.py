from django.http import HttpResponse
from django.shortcuts import render
import json
import datetime as dt
import pytz
import pricecheck.service_pricecheck as service_pricecheck
from pricecheck.dto import *

AMAZON_NAME_ID = 'productTitle'
AMAZON_PRICE_IDS = ['price_inside_buybox', 'newBuyBoxPrice']

def tests(request):
    return render(request, 'pricecheck/test.html', {})


def index(request):
    context = service_pricecheck.get_index_context()
    return render(request, 'pricecheck/index.html', context)


def validate(request):
    print('view.validate')
    if request.method == 'POST':
        url_text = request.POST.get('url')
        response_data = {}
        if url_text.strip() != '':
            validation = service_pricecheck.validate_url(url_text, AMAZON_NAME_ID, AMAZON_PRICE_IDS)
            if validation['error'] is None:
                response_data['status'] = 'ok'
                response_data['product_date'] = dt.datetime.now().strftime('%d %B %Y, %H:%M')
                response_data['product_name'] = validation['product_name']
                response_data['product_price'] = validation['product_price']
                response_data['product_currency'] = validation['product_currency']
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        response_data['status'] = 'No valid URL detected'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"error": "validation error"}),
            content_type="application/json"
        )


def add_product(request):
    product_dto = ProductDTO()
    if request.method == 'POST':
        product_dto.name = request.POST['product_name']
        product_dto.price = request.POST['product_price']
        product_dto.currency = request.POST['product_currency']
        product_dto.username = request.POST['username']
        product_dto.email = request.POST['email']
        product_dto.url = request.POST['link']
        product_dto.duration = request.POST.get('duration') # in days
        product_dto.promocode = request.POST['promocode']
    print(product_dto)
    context = service_pricecheck.get_add_product_context(product_dto)
    return render(request, 'pricecheck/add_product_result.html', context)


def product_info(request):
    product_dto = ProductDTO()
    if request.method == 'POST':
        product_dto.track_code = request.POST['track_code']
    context = service_pricecheck.get_product_info_context(product_dto)
    print(context)
    return render(request, 'pricecheck/info_product.html', context)


'''
def numbers(request):
    day = ''
    if request.method == "POST":
        day = request.POST['day']
    print('day = ' + day)
    if day == '':
        day = '0';
    context = service_covid.get_covid_numbers_data(day)
    return render(request, 'owid/numbers.html', context)

def numbers_json(request):
    data = {'country': ''}
    if request.method == 'GET':
        country = request.GET.get('country')
        days = request.GET.get('days')
        data_list = service_covid.get_covid_numbers_data_as_dict(country, days)
        if data_list:
            data['country'] = list(data_list)
    return JsonResponse(data, safe=False)
'''









