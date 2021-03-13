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


def get_charts():
    nums = [4004]
    charts = []
    catalogueDB = repo.get_latest_catalogue()
    catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    for num in nums:
        if catalogueDB.chart_set.filter(number=num).exists():
            chartDB = catalogueDB.chart_set.get(number=num)
            chart = service_converters.chartDB_2_chartDTO(chartDB)
            charts.append(chart)
            print(charts[0])
            print(charts[0].polygons)

    return charts


#service_parse.import_catalogue_from_file(SNC_CATALOGUE_FILE)

delete_catalogue_range(23, 50)


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

#get_charts()


#print(service_geojson.generate_geojson(' '))



'''
def get_panels():
    obj = untangle.parse(SNC_CATALOGUE_FILE)
    # panels
    try:
        
        positions = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart[6].Metadata.Panel[0].Polygon.Position
        panels = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart[6].Metadata.Panel
        print('panels: ' + str(len(panels)))
        if len(panels) > 0:  # redundant
            for pan in panels:
                print('panel: ' + pan.PanelAreaName.cdata)
                # panel = Panel()
                # panel.chart = chart
                # panel.panel_id = pan.PanelID.cdata
                # panel.area = pan.PanelAreaName.cdata
                # panel.name = pan.PanelName.cdata
                # panel.scale = pan.PanelScale.cdata
                # panel.save(using=snc)
                # panel polygon
                # panel_polygon = PanelPolygon()
                # panel_polygon.panel = panel
                # panel_polygon.save(using=snc)
                for p in positions:
                    # # panel_position = PanelPosition()
                    # panel_position.panel_polygon = panel_position
                    # panel_position.lat = p['latitude']
                    # panel_position.lon = p['longitude']
                    # panel_position.save(using=snc)
                print('--------- polygon type: panel, saved')
    except:
        pass

'''

'''
catalogue = import_catalogue(get_xml_object(SNC_CATALOGUE_FILE))
print(catalogue.file_identifier)
print(catalogue.organisation_name)
print(catalogue.fax)
print(catalogue.phone)
print(catalogue.deliveryPoint)
print(catalogue.city)
print(catalogue.administrative_area)
print(catalogue.postal_code)
print(catalogue.country)
print(catalogue.email)
print(catalogue.date)
obj = untangle.parse(SNC_CATALOGUE_FILE)s

# untangle ------------------------------------------------------------------
obj = untangle.parse(SNC_CATALOGUE_FILE)

#print(obj.UKHOCatalogueFile.BaseFileMetadata.MD_FileIdentifier.cdata)

#print(obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart[0].ShortName.cdata)

print('snc:')

snc_list = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart
print(len(snc_list))

snc_slice = snc_list[3500:]
print(len(snc_slice))


for item in snc_list:
    # print(item.ShortName.cdata)
    # print(item.Metadata.DatasetTitle.cdata)
    # print(item.Metadata.Scale.cdata)
    # print(item.Metadata.GeographicLimit.Polygon)


    # pos = item.Metadata.GeographicLimit.Polygon.Position
    # for p in pos:
    #     print(p['latitude'] + ', ' + p['longitude'])

    try:
        boundbox = item.Metadata.GeographicLimit.BoundingBox
        print(item.ShortName.cdata)
        print(boundbox.NorthLimit.cdata)
    except:
        pass

'''

















