# VARIABLES

APP_BASE = 'http://127.0.0.1:8000/pricecheck'
# APP_BASE = 'http://pc.latidude99.com/pricecheck'

# /confirm_product?code=fsWeSFSlkjhLkngv

AMAZON_NAME_ID = 'productTitle'
AMAZON_PRICE_IDS = ['price_inside_buybox', 'newBuyBoxPrice']

MAX_PRODUCT_TRACKED = 10

BACK_PATTERN1 = 'images/vintage-concrete.png'

# prod
proxies_prod = {
    "http": "http://87.173.188.201:8080",
    "https": "http://18.159.213.142:3128",
    # "http": "http://poell.online",
    # "http": "http://45.245.212.164",
    # "http": "http://95.216.194.46:1081",
    # "http": "http://138.197.14.103:3128",
    # "http": "http://36.89.126.183:8080",
    # "http": "http://189.61.87.178:8080",
    # "http": "http://207.144.111.230:8080",
    # "http": "http://138.59.150.198:8080",

    #    "https": "http://172.104.143.223:8080"
}

# dev
proxies = {
    "http": '78.141.242.65:8080',
    "https": '78.141.242.65:8080'
    # "http": "http://146.120.214.62:8080",
    #  "http": "http://83.242.123.248:8080",
    # "http": "http://187.95.114.125:3128",
    # "http": "http://195.53.49.11:3128",
    # "http": "http://195.154.58.0:8080",
    # "http": "http://68.188.63.149:8080",
    # "http": "http://91.126.239.175:8080",
    # "http": "http://3.135.219.183:3128",
    # "http": "http://154.202.56.21:3128",
    # "https": "http://197.97.95.98:8080",

}



# proxiy sources

PROXY_POOL_NEW = 'https://free-proxy-list.net/'
PROXY_POOL_SSL = 'https://sslproxies.org/'
PROXY_POOL_ANON = 'https://free-proxy-list.net/anonymous-proxy.html'
PROXY_POOL_UK = 'https://free-proxy-list.net/uk-proxy.html'

PROXY_POOL = PROXY_POOL_UK














