# CONSTANTS

import main.secrets as secrets
from latidude99.settings import SNC_STATIC_DATA_FOLDER, SNC_DATA_FOLDER

#APP_BASE = 'http://127.0.0.1:8000/snc'
APP_BASE = 'http://pc.latidude99.com/snc'

SNC_DATA = 'data/'
SNC_CATALOGUE_FILE = SNC_DATA_FOLDER + 'snc_catalogue.xml'
SNC_GEOJSON_FILE = SNC_DATA_FOLDER + 'charts_all.json'




SNC_SCALE_1_HTML = 'data/scale_1_html'
SNC_SCALE_2_HTML = 'data/scale_2_html'
SNC_SCALE_3_HTML = 'data/scale_3_html'
SNC_SCALE_4_HTML = 'data/scale_4_html'
SNC_SCALE_5_HTML = 'data/scale_5_html'
SNC_SCALE_6_HTML = 'data/scale_6_html'
SNC_SCALE_7_HTML = 'data/scale_7_html'


GOOGLE_API_KEY_DEV_UN = secrets.GOOGLE_MAPS_JAVASCRIPT_API_KEY_DEV_UNRESTRICTED
GOOGLE_API_KEY_DEV = secrets.GOOGLE_MAPS_JAVASCRIPT_API_KEY_DEV
GOOGLE_API_KEY_PROD = secrets.GOOGLE_MAPS_JAVASCRIPT_API_KEY_PROD

MAP_ZOOM = '5'
MAP_CENTRE = '{lat: 54.15, lng: -2.72}'
MAP_BOUNDS = ''


# SCALE and SCALE_TEXT used in DB - do not change!
SCALE_0 = 0
SCALE_1 = 4000
SCALE_2 = 22000
SCALE_3 = 90000
SCALE_4 = 350000
SCALE_5 = 1500000
SCALE_6 = 5000000


SCALE_ALL_TEXT = 'all scales'
SCALE_1_TEXT = '> 1:4,000'
SCALE_2_TEXT = '1:4,000 - 1:22,000'
SCALE_3_TEXT = '1:22,000 - 1:90,000'
SCALE_4_TEXT = '1:90,000 - 1:350,000'
SCALE_5_TEXT = '1:350,000 - 1:1,500,000'
SCALE_6_TEXT = '1:1,500,000 - 5,000,000'
SCALE_7_TEXT = '< 1:5,000,000'

SCALE_RANGE_ALL = [
         SCALE_1_TEXT,
         SCALE_2_TEXT,
         SCALE_3_TEXT,
         SCALE_4_TEXT,
         SCALE_5_TEXT,
         SCALE_6_TEXT,
         SCALE_7_TEXT,
         SCALE_ALL_TEXT,
         ]

CHART_COLOUR = '#000099'
PANEL_COLOUR = '#006600'



