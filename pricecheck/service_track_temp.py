#import django
#django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email as service_email
import latidude99.settings as settings
import datetime as dt
import pytz
from django.utils import timezone
from pricecheck.text import *
from pricecheck.models import *
from pricecheck.dto import *
from pricecheck.service_converters import *
import string, random
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure


# not used
def validate_url(url, product_id, price_ids):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    page = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(page.content, 'html.parser')
    div_product = soup.find(id=product_id)
    div_price = None
    for id in price_ids:
        div_price = soup.find(id=id)
        if div_price != None:  # found the working price tag
            break
    print(url)
    print(product_id)
    print(price_ids)
    print(div_price)
    validation = {}
    if div_price != None:
        product_name = div_product.get_text().strip()
        product_price = div_price.get_text().strip()
        validation['product_name'] = product_name
        validation['product_price'] = product_price[1:]
        validation['product_currency'] = product_price[:1]
        validation['error'] = None
    else:
        validation['product_name'] = ''
        validation['product_price'] = ''
        validation['product_currency'] = ''
        validation['error'] = 'No price found'
    return validation




def update_prices(track_code):
    code = track_code.strip()
    if code != '' and len(code) < 16:# incorrect track_code
        error = code + ' - Invalid tracking code: the code has to be 16 characters long.'
        return error
    elif len(code) == 16: # correct track_code
        try:
            product = Product.objects.using('pricecheck_34').get(track_code=code)
            current_price = check_price(product,AMAZON_NAME_ID, AMAZON_PRICE_IDS)
            price = Price(product=product, price=current_price[1:], date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC), currency=current_price[0])
            price.save(using='pricecheck_34')
            return code + ' product price updated.'
        except Product.DoesNotExist:
            error = code + ' - Invalid tracking code: no product found.'
            return error
    else: # update all by passing '' as track_code parameter
        products = Product.objects.using('pricecheck_34').filter(confirmed=True,tracked=True)
        for product in products[:1]:
            if product.confirmed:
                timedelta = product.end_date - dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
                if timedelta.days < 0:
                    product.tracked = False
                    product.save(using='pricecheck_34')
                    continue
                prices = product.price_set.all()
                price_values = [x.price for x in prices]
                initial_price = price_values[0]
                latest_price = price_values[-1]
                current_price = check_price(product, AMAZON_NAME_ID, AMAZON_PRICE_IDS)
                price = Price(product=product,
                              price=current_price[1:],
                              date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC),
                              currency=current_price[0])
                price.save(using='pricecheck_34')
                product = Product.objects.using('pricecheck_34').get(track_code=product.track_code)
                product_dto = convert_product_db2dto(product)
                product_dto.track_link = APP_BASE + '/product?track_code=' + product.track_code
                product_dto.stop_link = APP_BASE + '/product?stop_code=' + product.stop_code
                product_dto.app_link = APP_BASE


                x = product_dto.price_labels
                y = product_dto.price_values

                x_pos = [i for i, _ in enumerate(x)]
                plt.bar(x_pos, y)

                plt.title(product_dto.name, fontsize=12)
                plt.xlabel('time', fontsize=10)
                plt.ylabel(product_dto.currency, fontsize=10)
                plt.grid(True)
                plt.xticks(x_pos, x, rotation='vertical', fontsize=6)
                plt.margins(0.2)
                plt.subplots_adjust(bottom=0.15)
             #   plt.rcParams["figure.figsize"] = (20, 3)
                my_dpi = 96
                plt.figure(figsize=(800 / my_dpi, 800 / my_dpi), dpi=my_dpi)
                plt.savefig('my_fig.png', dpi=my_dpi)
                plt.savefig('my_fig.png', dpi=my_dpi * 2)

                plt.show()

                sub = 'Price Tracking Service: ' + product_dto.name
                templ = 'pricecheck/email_check_product.html'

                # if latest_price < float(current_price[1:]) and float(current_price[1:]) - latest_price >= product.threshold_down:
                #     product_dto.price_diff = float(current_price[1:]) - latest_price
                #     service_email.send_email(product_dto, sub, templ)
                #     print('threshold_down')
                #     print('current_price')
                #     print(float(current_price[1:]))
                # elif latest_price > float(current_price[1:]) and latest_price - float(current_price[1:]) >= product.threshold_up:
                #     product_dto.price_diff = float(current_price[1:]) - latest_price
                #     service_email.send_email(product_dto, sub, templ)
                #     print('threshold_up')
                #     print('current_price')
                #     print(float(current_price[1:]))


                service_email.send_email(product_dto, sub, templ)

                print('price updated for: ' + product.name)
        return str(len(products)) + ' products prices updated.'


def check_price(product, name_tag, price_tags):
    product_name = ''
    product_price = ''

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(product.url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_product = soup.find(id=name_tag)
    div_price = None
    for id in price_tags:
        div_price = soup.find(id=id)
        if div_price != None:  # found the working price tag
            break
    if div_price != None:
        product_name = div_product.get_text().strip()
        product_price = div_price.get_text().strip()
    return product_price





#update_prices('')



'''

<script>
    window.onload = function () {
        var URI;
        var ctx = document.getElementById('chart').getContext('2d');
        var data = {
            labels: [
                {% for item in  product_dto.price_labels %}
                    "{{ item }}",
                {% endfor %}
            ],
            datasets: [{
                label: '{{product_dto.currency}}',
                data: [
                    {% for item in product_dto.price_values %}
                        "{{ item }}",
                    {% endfor %}
                ],
                backgroundColor: "rgba(255, 0, 0, 0.50)",
                borderColor: "red",
                borderWidth: 0,
                barPercentage: 0.9,
                barThickness: '10',
            }]
        };
        var options = {
            scales: {
                xAxes: [{
                    gridLines: {
                        color: "rgba(0, 0, 0, 0.15)",
                        zeroLineColor: "rgba(0, 0, 0, 0.5)",
                    },
                    ticks: {
                        fontColor: "rgba(0, 0, 0, 0.8)",
                    }
                }],
                yAxes: [{
                    gridLines: {
                        color: "rgba(0, 0, 0, 0.15)",
                        zeroLineColor: "rgba(0, 0, 0, 0.5)",
                    },
                    ticks: {
                        beginAtZero: true,
                        fontColor: "rgba(0, 0, 0, 0.8)",
                        userCallback: function (value, index, values) {
                            return value.toLocaleString();   // this is all we need
                        },
                    }
                }]

            },
            legend: {
                display: false,
                labels: {
                    fontColor: 'rgb(255, 0, 0)'
                }
            },
            title: {
                display: false,
                text: '{{ product_dto.currency }}'
            },
            layout: {
                padding: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 0,
                }
            },
            elements: {
                point: {
                    radius: 1,
                    hoverRadius: 5,
                }
            },
            hover: {
                mode: 'index',
                intersect: false
            },
            responsive: true,
            tooltips: {
                enabled: true,
                mode: 'index',
                intersect: false,
                yAlign: 'top',
                callbacks: {
                    label: function (tooltipItem, data) {
                        var tooltipValue = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                        return parseInt(tooltipValue).toLocaleString();
                    }
                },
            },
            animation: {
                onComplete: done
            },
        };

        var prices = new Chart(ctx, {
            type: 'bar',
            data: data,
            options: options,
        });

        function done() {
            URI = prices.toBase64Image();
            console.log(URI);
            $('#image').attr("src", URI);
        }

        var URI_remote;
        {#$('#remote').attr("src", URI_remote);#}

        {#console.log(document.getElementById('image').innerText);#}
        {#document.getElementById('image').src = prices.toBase64Image();#}
    };

</script>

 <img id="image" src="" alt="canvas chart" width="80%">

 

'''