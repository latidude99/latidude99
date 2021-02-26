# VARIABLES

#APP_BASE = 'http://127.0.0.1:8000/pricecheck'
APP_BASE = 'http://pc.latidude99.com/pricecheck'

# /confirm_product?code=fsWeSFSlkjhLkngv

AMAZON_WEBSITE = 'amazon.co.uk'
AMAZON_NAME_ID = 'productTitle'
AMAZON_PRICE_IDS = ['price_inside_buybox', 'newBuyBoxPrice']

LEWIS_WEBSITE = 'johnlewis.com'
LEWIS_NAME_CLASS = 'ProductHeader__title--2klR1'
LEWIS_PRICE_CLASS = 'ProductPrice__item--1p_iL'

CURRYS_WEBSITE = 'currys.co.uk'
CURRYS_NAME_CLASS = 'page-title'
CURRYS_PRICE_CLASS = 'amounts'


MAX_PRODUCT_TRACKED = 10

BACK_PATTERN1 = 'images/vintage-concrete.png'

# prod
proxies_prod = {
     "http": "http://85.214.91.218:3128",
     "https": "http://35.175.242.158:3128",
}

# dev
proxies = {
    "http": "http://139.180.147.242:8080",
    "https": "http://139.180.147.242:8080",

}



# proxiy sources

PROXY_POOL_NEW = 'https://free-proxy-list.net/'
PROXY_POOL_SSL = 'https://sslproxies.org/'
PROXY_POOL_ANON = 'https://free-proxy-list.net/anonymous-proxy.html'
PROXY_POOL_UK = 'https://free-proxy-list.net/uk-proxy.html'

PROXY_POOL = PROXY_POOL_NEW














