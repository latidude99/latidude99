#import django
#django.setup()

import untangle
#import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.position
import snc.utils as utils
from snc.const import *
from snc.models import *
import datetime as dt
import pytz



# tools ------------------------------------------------------------------


def delete_catalogue(num):
    Catalogue.objects.using('snc').filter(id=num).delete()
    print('catalogue id: ' + num + ' deleted')

def delete_all_catalogues():
    Catalogue.objects.using('snc').all().delete()
    print('all catalogues deleted')

def delete_all_charts():
    Chart.objects.using('snc').all().delete()
    print('all charts deleted')


# untangle ------------------------------------------------------------------

def import_catalogue_from_file(catalogue_file):
    obj = get_xml_object(catalogue_file)
    import_charts(obj)



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

    charts = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart
    for ch in charts:

        # # testing
        # num = ch.ShortName.cdata
        # if num != 'JP1085' and num != '1006':
        #     continue

        chart = Chart()
        chart.catalogue = catalogue
        if ch.ShortName.cdata == '4005':
            print(ch.ShortName.cdata)
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
            # max scale calculations, finding min scale denominator
            min = 100_000_000
            try:
                if chart.scale != '' and int(ch.scale.strip()) < min:
                    min = int(chart.scale.strip())
            except:
                pass

            # chart polygon
            try:
                positions = ch.Metadata.GeographicLimit.Polygon.Position
                chart_polygon = ChartPolygon()
                chart_polygon.chart = chart
                for pos in positions:
                    chart_position = ChartPosition()
                    chart_position.chart_polygon = chart_polygon
                    chart_position.lat = pos['latitude']
                    chart_position.lon = pos['longitude']
                print('--------- polygon type: chart, saved')
            except:
                pass

            try:
                check = ch.Metadata.GeographicLimit.Polygon[1].Position
                polygons = ch.Metadata.GeographicLimit.Polygon
                print(len(polygons))
                #print(polygons)
                north = 0
                south = 0
                west = 0
                east = 0
                for poly in polygons:
                    positions = poly.Position
                    print(len(positions))
                    for pos in positions:
                        if float(pos['latitude'].strip()) > north:
                            north = float(pos['latitude'].strip())
                        elif float(pos['latitude'].strip()) < south:
                            south = float(pos['latitude'].strip())
                        if float(pos['longitude'].strip()) > east:
                            east = float(pos['longitude'].strip())
                        elif float(pos['longitude'].strip()) < west:
                            west = float(pos['longitude'].strip())

                chart_polygon = ChartPolygon()
                chart_polygon.chart = chart

                # converts bounds to vertices
                northwest = ChartPosition()
                northwest.chart_polygon = chart_polygon
                northwest.lat = str(north)
                northwest.lon = str(west)
                print(northwest)

                northeast = ChartPosition()
                northeast.chart_polygon = chart_polygon
                northeast.lat = str(north)
                northeast.lon = str(east)
                print(northeast)

                southeast = ChartPosition()
                southeast.chart_polygon = chart_polygon
                southeast.lat = str(south)
                southeast.lon = str(east)
                print(southeast)

                southwest = ChartPosition()
                southwest.chart_polygon = chart_polygon
                southwest.lat = str(south)
                southwest.lon = str(west)
                print(southwest)

                print(chart)

            except:
                pass

                try:

                    # chart bounding box (no polygon)
                    boundbox = ch.Metadata.GeographicLimit.BoundingBox
                    print('in bounding box')
                    north = boundbox.NorthLimit.cdata
                    south = boundbox.SouthLimit.cdata
                    west = boundbox.WestLimit.cdata
                    east = boundbox.EastLimit.cdata

                    chart_polygon_bounding = ChartPolygon()
                    chart_polygon_bounding.chart = chart

                    # converts bounds to vertices
                    northwest = ChartPosition()
                    northwest.chart_polygon = chart_polygon_bounding
                    northwest.lat = north
                    northwest.lon = west
                    print(northwest)

                    northeast = ChartPosition()
                    northeast.chart_polygon = chart_polygon_bounding
                    northeast.lat = north
                    northeast.lon = east
                    print(northeast)

                    southeast = ChartPosition()
                    southeast.chart_polygon = chart_polygon_bounding
                    southeast.lat = south
                    southeast.lon = east
                    print(southeast)

                    southwest = ChartPosition()
                    southwest.chart_polygon = chart_polygon_bounding
                    southwest.lat = south
                    southwest.lon = west
                    print(southwest)

                    print('--------- polygon type: bounding box, saved')
                except:
                    pass

            try:
                #check = ch.Metadata.Panel[0].Polygon  # check if Panels have any Polygon
                panels = ch.Metadata.Panel
                if len(panels) > 0:
                    for pan in panels:
                        #print(pan)
                        panel = Panel()
                        panel.chart = chart
                        panel.panel_id = pan.PanelID.cdata
                        panel.area = pan.PanelAreaName.cdata
                        panel.name = pan.PanelName.cdata
                        panel.scale = pan.PanelScale.cdata
                        #panel.save(using='snc')
                        if panel.scale != '' and int(panel.scale.strip()) < min:
                            min = int(panel.scale.strip())
                        # panel polygons
                        polygons = pan.Polygon
                        if len(polygons) == 1:
                            panel_polygon = PanelPolygon()
                            panel_polygon.panel = panel
                            panel_polygon.save(using='snc')

                            positions = pan.Polygon.Position
                            for p in positions:
                                panel_position = PanelPosition()
                                panel_position.panel_polygon = panel_polygon
                                panel_position.lat = p['latitude']
                                panel_position.lon = p['longitude']
                                #panel_position.save(using='snc')
                            print('--------- polygon type: panel, saved')
                        elif len(polygons) > 1:
                            north = 0
                            south = 0
                            west = 0
                            east = 0
                            for poly in polygons:
                                positions = poly.Position
                                for pos in positions:
                                    if float(pos['latitude'].strip()) > north:
                                        north = float(pos['latitude'].strip())
                                    elif float(pos['latitude'].strip()) < south:
                                        south = float(pos['latitude'].strip())
                                    if float(pos['longitude'].strip()) > east:
                                        east = float(pos['longitude'].strip())
                                    elif float(pos['longitude'].strip()) < west:
                                        west = float(pos['longitude'].strip())

                            panel_polygon = PanelPolygon()
                            panel_polygon.chart = chart

                            # converts bounds to vertices
                            northwest = PanelPosition()
                            northwest.panel_polygon = panel_polygon
                            northwest.lat = str(north)
                            northwest.lon = str(west)
                            print(northwest)

                            northeast = PanelPosition()
                            northeast.panel_polygon = panel_polygon
                            northeast.lat = str(north)
                            northeast.lon = str(east)
                            print(northeast)

                            southeast = PanelPosition()
                            southeast.panel_polygon = panel_polygon
                            southeast.lat = str(south)
                            southeast.lon = str(east)
                            print(southeast)

                            southwest = PanelPosition()
                            southwest.panel_polygon = panel_polygon
                            southwest.lat = str(south)
                            southwest.lon = str(west)
                            print(southwest)
                            print(min)
            except:
                pass












