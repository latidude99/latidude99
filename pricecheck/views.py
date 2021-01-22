from django.http import HttpResponse
from django.shortcuts import render
import json
import datetime as dt
import pytz
import pricecheck.service_pricecheck as service_pricecheck



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
        validation = service_pricecheck.validate_url(url_text)
        response_data['product_date'] = dt.datetime.now().strftime('%d %B %Y, %H:%M')
        response_data['product_name'] = validation['product_name']
        response_data['product_price'] = validation['product_price']
        response_data['product_currency'] = validation['product_currency']
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"error": "validation error"}),
            content_type="application/json"
        )