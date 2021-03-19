import django
django.setup()

import untangle
#import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.position
from snc.models import *
from snc.const import *
import snc.service_parse as service_parse
import snc.service_parse_2 as service_parse_2
import snc.service_converters as service_converters
import snc.utils as utils
import snc.repository as repo
import snc.service_geojson as service_geojson


def delete_catalogue_range(a, b):
    for i in range(a, b):
        print(i)
        service_parse.delete_catalogue(i)


def get_charts(nums):
    charts = []
    catalogueDB = repo.get_latest_catalogue()
    catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    for num in nums:
        if catalogueDB.chart_set.filter(number=num).exists():
            chartDB = catalogueDB.chart_set.get(number=num)
            chart = service_converters.chartDB_2_chartDTO(chartDB)
            charts.append(chart)
            # print(charts[0])
            # print(charts[0].polygons)

    return charts


#service_parse.import_catalogue_from_file(SNC_CATALOGUE_FILE)

#delete_catalogue_range(50, 60)


#service_parse.delete_all_charts()

#service_parse.delete_all_catalogues()

#service_parse.delete_catalogue('23')

#utils.print_chart_detail()

#utils.add_scale_category()


#print(len(repo.find_charts_all()))

# print(len(repo.find_charts_SCALE_1()))
# print(len(repo.find_charts_SCALE_2()))
# print(len(repo.find_charts_SCALE_3()))
# print(len(repo.find_charts_SCALE_4()))
# print(len(repo.find_charts_SCALE_5()))
# print(len(repo.find_charts_SCALE_6()))
# print(len(repo.find_charts_SCALE_7()))


# chartsDB = repo.find_charts_SCALE_1()
# print('folio-------------------')
# print(chartsDB[0].folio)
# print(chartsDB[45].folio)
# print(chartsDB[455].folio)


# obj = untangle.parse(SNC_CATALOGUE_FILE)
# charts = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart

#service_parse.import_catalogue_from_file(SNC_CATALOGUE_FILE)



#charts = get_charts([4720])

#chartsDB = repo.find_charts_all()
#charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
#charts = repo.find_charts([1330, 2, 32, 34])
#print('number of charts: ' + str(len(charts)))

print(service_geojson.generate_geojson_and_save_db([SCALE_7_TEXT]))
















