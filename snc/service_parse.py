#import django
#django.setup()

import untangle
import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.point
from snc.const import *
from snc.models import *
import datetime as dt
import pytz


def delete_all_catalogues():
    Catalogue.objects.using('snc').all().delete()
    print('all catalogues deleted')

def delete_all_charts():
    Chart.objects.using('snc').all().delete()
    print('all charts deleted')

# untangle ------------------------------------------------------------------

def get_xml_object(SNC_CATALOGUE_FILE):
    obj = untangle.parse(SNC_CATALOGUE_FILE)
    return obj


def import_catalogue(obj):
    catalogue = Catalogue()
    meta = obj.UKHOCatalogueFile.BaseFileMetadata
    catalogue.file_identifier = meta.MD_FileIdentifier.cdata
    catalogue.organisation_name = meta.MD_PointOfContact.ResponsibleParty.organisationName.cdata
    catalogue.fax = meta.MD_PointOfContact.ResponsibleParty.contactInfo.fax.cdata
    catalogue.phone = meta.MD_PointOfContact.ResponsibleParty.contactInfo.phone.cdata
    catalogue.deliveryPoint = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.deliveryPoint.cdata
    catalogue.city = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.city.cdata
    catalogue.administrative_area = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.administrativeArea.cdata
    catalogue.postal_code = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.postalCode.cdata
    catalogue.country = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.country.cdata
    catalogue.email = meta.MD_PointOfContact.ResponsibleParty.contactInfo.address.electronicMailAddress.cdata
    catalogue.date = dt.datetime.strptime(meta.MD_DateStamp.cdata, '%Y-%m-%d').date()
     #date_stanp.pytz.timezone('Europe/London')

    return catalogue


def import_charts(obj):
    catalogue = import_catalogue(obj)
    catalogue.save(using='snc')
    charts = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart
    for ch in charts:
        chart = Chart()
        chart.catalogue = catalogue
        chart.number = ch.ShortName.cdata
        chart.title = ch.Metadata.DatasetTitle.cdata
        chart.scale = ch.Metadata.Scale.cdata
        chart.folio = ch.Metadata.Folio.ID.cdata
        chart.cat_number = ch.Metadata.CatalogueNumber.cdata
        chart.int_number = ''
        chart.status = ch.Metadata.Status.ChartStatus.cdata
        chart.status_date = ch.Metadata.Status.ChartStatus['date']
        chart.new_edition_date = ch.Metadata.ChartNewEditionDate.cdata
        chart.import_date = dt.datetime.now(pytz.timezone('Europe/London'))
        chart.save(using='snc')
        try:
            positions = ch.Metadata.GeographicLimit.Polygon.Position
            chart_polygon = ChartPolygon()
            for p in positions:
                chart_position = ChartPosition()
                chart_position.chart_polygon = chart_polygon
                chart_position.lat = p['latitude']
                chart_position.lon = p['longitude']
        except:
            pass





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


'''
obj = untangle.parse(SNC_CATALOGUE_FILE)

print(obj.UKHOCatalogueFile.BaseFileMetadata.MD_FileIdentifier.cdata)
print(obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart[0].ShortName.cdata)
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

