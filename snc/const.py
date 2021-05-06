# CONSTANTS

import main.secrets as secrets
from latidude99.settings import SNC_STATIC_DATA_FOLDER, SNC_DATA_FOLDER

#APP_BASE = 'http://127.0.0.1:8000/snc'
APP_BASE = 'http://pc.latidude99.com/snc'

DB_LOCAL = 'default'
DB_REMOTE = 'snc'

DB_SNC = DB_LOCAL


URL_UKHO_BASE = "https://enavigator.ukho.gov.uk/"
URL_UKHO_LOGIN = "https://enavigator.ukho.gov.uk/Login"
URL_UKHO_DOWNLOAD = "https://enavigator.ukho.gov.uk/Download"

SNC_DATA = 'data/'
SNC_CATALOGUE_FILE = SNC_DATA_FOLDER + 'snc_catalogue.xml'
SNC_GEOJSON_FILE = SNC_DATA_FOLDER + 'charts_all.json'


URL_CHS_ARCGIS_HUB = 'https://hub.arcgis.com/datasets/5932ed16cc7a4cdfad78d15830bbeaba_0/data?geometry=17.740%2C40.158%2C168.560%2C83.789'
URL_CHS_GEOJSON = 'https://opendata.arcgis.com/datasets/5932ed16cc7a4cdfad78d15830bbeaba_0.geojson'

CHS_GEOJSON_FILE = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits.geojson'
CHS_GEOJSON_FILE_EDITED = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-edited.geojson'

CHS_GEOJSON_FILE_SCALE_1 = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-scale1.geojson'
CHS_GEOJSON_FILE_SCALE_2 = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-scale2.geojson'
CHS_GEOJSON_FILE_SCALE_3 = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-scale3.geojson'
CHS_GEOJSON_FILE_SCALE_4 = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-scale4.geojson'
CHS_GEOJSON_FILE_SCALE_5 = SNC_DATA_FOLDER + 'Paper_Nautical_Chart_Limits-scale5.geojson'

CHS_SCALE_1 = 20000 # < 20_000
CHS_SCALE_2 = 50000 # 20_000 - 50_000
CHS_SCALE_3 = 150000 # 50_000 - 150_000
CHS_SCALE_4 = 500000 # 150_000 - 500_000
# CHS_SCALE_5 = 500_000  #  > 500_000




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

# starts centered on British Isles
MAP_ZOOM = '3'
MAP_ZOOM_CHS = '3'
MAP_CENTRE = '{lat: 18, lng: -28}'
MAP_CENTRE_CHS = '{lat: 70., lng: -103}'
MAP_BOUNDS = ''

PORT_APPROACHES = 'port_approaches'

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



