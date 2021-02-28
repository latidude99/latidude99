#import django
#django.setup()

import untangle
import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.point
from snc.const import *
from snc.models import *
import datetime as dt
import pytz



# tools ------------------------------------------------------------------

def delete_all_catalogues():
    Catalogue.objects.using('snc').all().delete()
    print('all catalogues deleted')

def delete_all_charts():
    Chart.objects.using('snc').all().delete()
    print('all charts deleted')


# untangle ------------------------------------------------------------------

def import_calogue_from_file(catalogue_file):
    obj = get_xml_object(catalogue_file)
    import_charts(obj)
    print('file parsed, all charts imported')

def get_xml_object(catalogue_file):
    obj = untangle.parse(catalogue_file)
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
    for ch in charts[6:8]:
        chart = Chart()
        chart.catalogue = catalogue
        chart.number = ch.ShortName.cdata
        chart.title = ch.Metadata.DatasetTitle.cdata
        try:
            chart.scale = ch.Metadata.Scale.cdata
        except:
            pass
        try:
            chart.folio = ch.Metadata.Folio.ID.cdata
        except:
            pass
        try:
            chart.last_nm_number = ch.Metadata.LastNMNumber.cdata
            chart.last_nm_date = ch.Metadata.LastNMDate.cdata
        except:
            pass
        chart.cat_number = ch.Metadata.CatalogueNumber.cdata
        chart.int_number = ''
        chart.status = ch.Metadata.Status.ChartStatus.cdata
        chart.status_date = ch.Metadata.Status.ChartStatus['date']
        chart.new_edition_date = ch.Metadata.ChartNewEditionDate.cdata
        chart.import_date = dt.datetime.now(pytz.timezone('Europe/London'))
        chart.save(using='snc')
        print('chart ' + chart.number + ', saved')

        # chart polygon
        try:
            positions = ch.Metadata.GeographicLimit.Polygon.Position
            print(positions)
            chart_polygon = ChartPolygon()
            chart_polygon.chart = chart
            chart_polygon.save(using='snc')
            for pos in positions:
                chart_position = ChartPosition()
                chart_position.chart_polygon = chart_polygon
                chart_position.lat = pos['latitude']
                chart_position.lon = pos['longitude']
                chart_position.save(using='snc')
            print('--------- polygon type: chart, saved')
        except:
            # chart bounding box (no polygon)
            try:
                boundbox = ch.Metadata.GeographicLimit.BoundingBox
                north = boundbox.NorthLimit.cdata
                south = boundbox.SouthLimit.cdata
                west = boundbox.WestLimit.cdata
                east = boundbox.EastLimit.cdata

                chart_polygon_bounding = ChartPolygon()
                chart_polygon_bounding.save(using='snc')

                # converts bounds to vertices
                northwest = ChartPosition()
                northwest.chart_polygon = chart_polygon_bounding
                northwest.lat = north
                northwest.lon = west
                northwest.save(using='snc')

                norteast = ChartPosition()
                norteast.chart_polygon = chart_polygon_bounding
                norteast.lat = north
                norteast.lon = east
                norteast.save(using='snc')

                southeast = ChartPosition()
                southeast.chart_polygon = chart_polygon_bounding
                southeast.lat = south
                southeast.lon = east
                southeast.save(using='snc')

                southwest = ChartPosition()
                southwest.chart_polygon = chart_polygon_bounding
                southwest.lat = south
                southwest.lon = west
                southwest.save(using='snc')

                print('--------- polygon type: bounding box, saved')
            except:
                pass
            pass

        # panels
        try:
            panels = ch.Metadata.Panel
            print('panels: ' + str(len(panels)))
            if len(panels) > 0:
                for pan in panels:
                    panel = Panel()
                    panel.chart = chart
                    panel.panel_id = pan.PanelID.cdata
                    panel.area = pan.PanelAreaName.cdata
                    panel.name = pan.PanelName.cdata
                    panel.scale = pan.PanelScale.cdata
                    panel.save(using='snc')
                    # panel polygon
                    panel_polygon = PanelPolygon()
                    panel_polygon.panel = panel
                    panel_polygon.save(using='snc')

                    positions = pan.Polygon.Position
                    for p in positions:
                        panel_position = PanelPosition()
                        panel_position.panel_polygon = panel_polygon
                        panel_position.lat = p['latitude']
                        panel_position.lon = p['longitude']
                        panel_position.save(using='snc')
                    print('--------- polygon type: panel, saved')
        except:
            pass

        # NMs
        try:
            notices = ch.Metadata.NoticesToMariners
            for n in notices:
                notice = Notice()
                notice.chart = chart
                notice.year = n.Year.cdata
                notice.week = n.Week.cdata
                notice.number = n.Number.cdata
                notice.type = n.Type.cdata
                notice.save(using='snc')
                print('--------- notice: ' + notice.number + ', saved')
        except:
            pass

    # sets import process finished flag to true
    catalogue.ready = True
    catalogue.save(using='snc')
    print('calogue ready set to True')













