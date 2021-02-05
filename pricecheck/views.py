from django.http import HttpResponse
from django.shortcuts import render
import json
import datetime as dt
import pytz
import pricecheck.service as service
import pricecheck.service_info as service_info
import pricecheck.service_add as service_add
import pricecheck.service_track as service_track
from pricecheck.dto import *
from pricecheck.text import *
from pricecheck.const import *


def tests(request):
    return render(request, 'pricecheck/test.html', {})


def index(request):
    context = service.get_index_context()
    return render(request, 'pricecheck/index.html', context)


def validate(request):
    print('view.validate')
    if request.method == 'POST':
        url_text = request.POST.get('url')
        response_data = {}
        if url_text.strip() != '':
            validation = service_info.validate_url(url_text, AMAZON_NAME_ID, AMAZON_PRICE_IDS)
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
    user_check = service_add.user_limit_duplicate_check(product_dto)
    print(user_check)
    if user_check[0]:
        user = user_check[1]
        context = service_add.get_add_product_context(user, product_dto)
        return render(request, 'pricecheck/add_product_result.html', context)
    else:
        errors = user_check[1]
        errors['email'] = product_dto.email
        errors['url'] = product_dto.url
        context = {**service.get_base_context(), **errors}
        return render(request, 'pricecheck/add_product_error_duplicate.html', context)


def confirm_product(request):
    confirm_code = ''
    if request.method == 'GET':
        confirm_code = request.GET.get('code')
    confirmation = service_add.get_context_confirm(confirm_code)
    context = confirmation[1]
    if confirmation[0]:
        return render(request, 'pricecheck/confirmation_ok.html', context)
    return render(request, 'pricecheck/confirmation_error.html', context)



def product(request):
    flag = ''
    product_dto = ProductDTO()
    if request.method == 'POST':
        if 'stop_code' in request.POST:
            product_dto.stop_code = request.POST['stop_code']
            flag = 'stop'
        elif 'track_code' in request.POST:
            product_dto.track_code = request.POST['track_code']
            flag = 'track'
    context = service_info.get_product_info_context(product_dto, flag)
    product_dto = context['product_dto']
    print(context)
    if product_dto.error1 != '':
        return render(request, 'pricecheck/index.html', context)
    if product_dto.error2 != '':
        return render(request, 'pricecheck/index.html', context)
    if product_dto.error != '':
        return render(request, 'pricecheck/product_error.html', context)
    if flag == 'stop':
        return render(request, 'pricecheck/stop_product.html', context)
    return render(request, 'pricecheck/info_product.html', context)










