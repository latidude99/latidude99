#import django
#django.setup()

import time
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email
import latidude99.settings as settings
from pricecheck.user_tmp import UserTmp
from django.template.loader import get_template
from django.template import Context

user = UserTmp('Piotr',
                'latidude99test@gmail.com',
                'https://www.amazon.co.uk/Audio-Technica-ATH-M50XBT-Wireless-Over-Ear-Headphones/dp/B07HKVCVSY',
                10)

print (UserTmp)

#url = "https://www.amazon.co.uk/Audio-Technica-ATH-M50XBT-Wireless-Over-Ear-Headphones/dp/B07HKVCVSY/ref=sr_1_1?crid=133JHFPXEQBEG&dchild=1&keywords=ath+m50x+bt&qid=1611159279&sprefix=ath+m50x%2Caps%2C170&sr=8-1"
#message = "The ATH-50XBT price"


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content

def check_item_price(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
#    spans = soup.find_all("span", {"class": "value"})
    div_product = soup.find(id="productTitle")
    div_price = soup.find(id="price_inside_buybox")
    if div_price is None:
        div_price = soup.find(id='newBuyBoxPrice')
    print(div_price)
    product = div_product.get_text().strip()
    price = div_price.get_text().strip()
    context = {'username': user.name,
               'product': product,
               'price': price}
    return context



def check():
    context = check_item_price(get_page_html(user.url))
    print(context)
    subject = 'Price check for ' + context['product']
    template = 'pricecheck/email_add_product.html'
    sender = settings.EMAIL_HOST_USER
    receiver = user.email
    #pricecheck.service_email.send(subject, template, context, sender, receiver)
    #print('pricecheck email sent to ' + user.email)



#while not check():
#    time.sleep(60)


#check_item_price(get_page_html(user.url))

#check()

'''
opening links pointing outside the host domain in a new tab:

$(document.links).filter(function() {
    return this.hostname != window.location.hostname;
}).attr('target', '_blank');
'''