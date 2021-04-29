# import django
# django.setup()

import untangle
# import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.position
import snc.service_geojson as service_geojson
import snc.utils as utils
from snc.const import *
from snc.models import *
import datetime as dt
import pytz


# tools ------------------------------------------------------------------
def delete_catalogue(num):
    Catalogue.objects.using(DB_SNC).filter(id=num).delete()
    print('catalogue id: ' + str(num) + ' deleted')


def delete_all_catalogues():
    Catalogue.objects.using(DB_SNC).all().delete()
    print('all catalogues deleted')


def delete_all_charts():
    Chart.objects.using(DB_SNC).all().delete()
    print('all charts deleted')


def delete_gejson_catalogue_id(ids):
    for id in ids:
        Geojson.objects.using(DB_SNC).filter(catalogue_id__exact=id).delete()
        print('deleted geojsons in catalogue_id ' + str(id))


# untangle ------------------------------------------------------------------
def parse_import_catalogue_with_geojson(catalogue_file):
    # parse and load catalogue to DB
    import_catalogue_from_file(catalogue_file)

    # generate set of geojson entries and save to DB (SCALE_1_TEXT etc)
    service_geojson.generate_geojson_and_save_db(SCALE_RANGE_ALL)

    # generate set of geojson entries and save to DB (SCALE_1_TEXT etc)
    service_geojson.generate_geojson_and_save_db_single_charts([])

    return 'ok - parsed - imported - generated geojson'


def import_catalogue_from_file(catalogue_file):
    obj = get_xml_object(catalogue_file)
    catalogue = ''
    catalogues = Catalogue.objects.using(DB_SNC).all()
    if catalogues:
        for c in reversed(catalogues):
            print('catalogue id :' + str(c.id))
            if c.ready:
                catalogue = c
                break
        file_catalogue_identifier = int(obj.UKHOCatalogueFile.BaseFileMetadata.MD_FileIdentifier.cdata)
        if file_catalogue_identifier > int(catalogue.file_identifier):
            import_charts(obj)
            print('file parsed, all charts imported')
        else:
            # import_charts(obj) # dev, to be removed for prod
            print('no new catalogue in the file')
    else:
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
    # date_stanp.pytz.timezone('Europe/London')

    return catalogue


def import_charts(obj):
    catalogue = import_catalogue(obj)
    catalogue.save(using=DB_SNC)

    charts = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart
    for ch in charts:

        # testing
        # num = ch.ShortName.cdata
        #  if num != 'JP1085' and num != '1006' and num != '4000' and num != '4004' and num != '1007' and num != '1330'\
        #          and num != '4005' and num != '4008' and num != '4012' and num != '4016' and num != '4007'
        #          and num != '4015':
        #  if num != '8028':
        #      continue

        chart = Chart()
        chart.catalogue = catalogue
        chart.number = ch.ShortName.cdata
        chart.title = ch.Metadata.DatasetTitle.cdata
        try:
            chart.scale = ch.Metadata.Scale.cdata
        except:
            chart.scale = ''
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
        chart.save(using=DB)
        print('chart ' + chart.number + ', saved')

        if chart.number == '4000':  # skips polygons for chart 4000, they don't display correctly
            continue

        # max scale calculations, finding min scale denominator
        min = 100_000_000
        try:
            if chart.scale != '' and int(chart.scale.strip()) < min:
                min = int(chart.scale.strip())
        except:
            pass

        # single main chart polygon
        try:
            positions = ch.Metadata.GeographicLimit.Polygon.Position
            print('inside single main polygon')
            chart_polygon = ChartPolygon()
            chart_polygon.chart = chart
            chart_polygon.save(using=DB)
            for pos in positions:
                chart_position = ChartPosition()
                chart_position.chart_polygon = chart_polygon
                chart_position.lat = pos['latitude']
                chart_position.lon = pos['longitude']
                chart_position.save(using=DB)
            print('--------- single main chart polygon, saved')
        except:
            pass

        # multiple main chart polygons
        try:
            check = ch.Metadata.GeographicLimit.Polygon[1].Position
            print('inside multiple main polygons')
            polygons = ch.Metadata.GeographicLimit.Polygon
            north = 0
            south = 0
            west = 0
            east = 0

            for poly in polygons:
                chart_polygon = ChartPolygon()
                chart_polygon.chart = chart
                chart_polygon.save(using=DB)

                positions = poly.Position
                for pos in positions:
                    chart_position = ChartPosition()
                    chart_position.chart_polygon = chart_polygon
                    chart_position.lat = pos['latitude']
                    chart_position.lon = pos['longitude']
                    chart_position.save(using=DB)

            #         if float(pos['latitude'].strip()) > north:
            #             north = float(pos['latitude'].strip())
            #         elif float(pos['latitude'].strip()) < south:
            #             south = float(pos['latitude'].strip())
            #         if float(pos['longitude'].strip()) > east:
            #             east = float(pos['longitude'].strip())
            #         elif float(pos['longitude'].strip()) < west:
            #             west = float(pos['longitude'].strip())
            #
            #
            # # converts bounds to vertices
            # northwest = ChartPosition()
            # northwest.chart_polygon = chart_polygon
            # northwest.lat = str(north)
            # northwest.lon = str(west)
            # northwest.save(using=DB)
            #
            # northeast = ChartPosition()
            # northeast.chart_polygon = chart_polygon
            # northeast.lat = str(north)
            # northeast.lon = str(east)
            # northeast.save(using=DB)
            #
            # southeast = ChartPosition()
            # southeast.chart_polygon = chart_polygon
            # southeast.lat = str(south)
            # southeast.lon = str(east)
            # southeast.save(using=DB)
            #
            # southwest = ChartPosition()
            # southwest.chart_polygon = chart_polygon
            # southwest.lat = str(south)
            # southwest.lon = str(west)
            # southwest.save(using=DB)
            print('multiple main polygons simplyfied and saved')

        except:
            pass

        # chart bounding box (no polygon)
        try:
            boundbox = ch.Metadata.GeographicLimit.BoundingBox
            print('inside bounding box')
            north = boundbox.NorthLimit.cdata
            south = boundbox.SouthLimit.cdata
            west = boundbox.WestLimit.cdata
            east = boundbox.EastLimit.cdata

            chart_polygon_bounding = ChartPolygon()
            chart_polygon_bounding.chart = chart
            chart_polygon_bounding.save(using=DB)

            # converts bounds to vertices
            northwest = ChartPosition()
            northwest.chart_polygon = chart_polygon_bounding
            northwest.lat = north
            northwest.lon = west
            northwest.save(using=DB)

            northeast = ChartPosition()
            northeast.chart_polygon = chart_polygon_bounding
            northeast.lat = north
            northeast.lon = east
            northeast.save(using=DB)

            southeast = ChartPosition()
            southeast.chart_polygon = chart_polygon_bounding
            southeast.lat = south
            southeast.lon = east
            southeast.save(using=DB)

            southwest = ChartPosition()
            southwest.chart_polygon = chart_polygon_bounding
            southwest.lat = south
            southwest.lon = west
            southwest.save(using=DB)

            print('--------- bounding box polygon saved')
        except:
            pass

        # single panel
        try:
            check = ch.Metadata.Panel.Polygon  # check if there is a single Panel
            panels = ch.Metadata.Panel
            print('inside single panel')
            if len(panels) > 0:
                for pan in panels:
                    panel = Panel()
                    panel.chart = chart
                    panel.panel_id = pan.PanelID.cdata
                    panel.area = pan.PanelAreaName.cdata
                    panel.name = pan.PanelName.cdata
                    panel.scale = pan.PanelScale.cdata
                    panel.save(using=DB)

                    if panel.scale != '' and int(panel.scale.strip()) < min:
                        min = int(panel.scale.strip())

                    # panel polygons
                    polygons = pan.Polygon
                    try:
                        # multiple panel polygons
                        check = polygons[1].Position
                        print('inside multiple panel polygons')
                        north = 0
                        south = 0
                        west = 0
                        east = 0

                        for poly in polygons:
                            panel_polygon = PanelPolygon()
                            panel_polygon.panel = panel
                            panel_polygon.save(using=DB)

                            positions = poly.Position
                            for pos in positions:
                                panel_position = PanelPosition()
                                panel_position.panel_polygon = panel_polygon
                                panel_position.lat = pos['latitude']
                                panel_position.lon = pos['longitude']
                                panel_position.save(using=DB)

                        #         if float(pos['latitude'].strip()) > north:
                        #             north = float(pos['latitude'].strip())
                        #         elif float(pos['latitude'].strip()) < south:
                        #             south = float(pos['latitude'].strip())
                        #         if float(pos['longitude'].strip()) > east:
                        #             east = float(pos['longitude'].strip()) -1
                        #         elif float(pos['longitude'].strip()) < west:
                        #             west = float(pos['longitude'].strip())
                        #
                        # # converts bounds to vertices
                        # southwest = PanelPosition()
                        # southwest.panel_polygon = panel_polygon
                        # southwest.lat = str(south)
                        # southwest.lon = str(west)
                        # southwest.save(using=DB)
                        #
                        # southeast = PanelPosition()
                        # southeast.panel_polygon = panel_polygon
                        # southeast.lat = str(south)
                        # southeast.lon = str(east)
                        # southeast.save(using=DB)
                        #
                        # northeast = PanelPosition()
                        # northeast.panel_polygon = panel_polygon
                        # northeast.lat = str(north)
                        # northeast.lon = str(east)
                        # northeast.save(using=DB)
                        #
                        # northwest = PanelPosition()
                        # northwest.panel_polygon = panel_polygon
                        # northwest.lat = str(north)
                        # northwest.lon = str(west)
                        # northwest.save(using=DB)

                        print('--------- multi polygon panel, saved')

                        # doesn't draw correctly
                        # PositionDTO(lat='83.75008', lon='-100.0')
                        # PositionDTO(lat='83.75008',lon='180.0')
                        # PositionDTO(lat='-78.75', lon='180.0')
                        # PositionDTO(lat='-78.75', lon='-100.0')

                        # print(northwest)
                        # print(northeast)
                        # print(southeast)
                        # print(southwest)
                        # print(panel_polygon.panelposition_set.all())

                    except:
                        try:
                            # single panel polygon
                            check = polygons.Position
                            print('inside single panel polygon')
                            panel_polygon = PanelPolygon()
                            panel_polygon.panel = panel
                            panel_polygon.save(using=DB)

                            positions = pan.Polygon.Position
                            for p in positions:
                                panel_position = PanelPosition()
                                panel_position.panel_polygon = panel_polygon
                                panel_position.lat = p['latitude']
                                panel_position.lon = p['longitude']
                                panel_position.save(using=DB)
                            print('--------- single polygon panel, saved')
                        except:
                            pass
        except:
            pass

        # multiple panels
        try:
            check = ch.Metadata.Panel[0].Polygon  # check if there are multiple Panels
            print('inside multiple panels')
            panels = ch.Metadata.Panel
            if len(panels) > 0:
                for pan in panels:
                    panel = Panel()
                    panel.chart = chart
                    panel.panel_id = pan.PanelID.cdata
                    panel.area = pan.PanelAreaName.cdata
                    panel.name = pan.PanelName.cdata
                    panel.scale = pan.PanelScale.cdata
                    panel.save(using=DB)

                    if panel.scale != '' and int(panel.scale.strip()) < min:
                        min = int(panel.scale.strip())

                    # panel polygons
                    polygons = pan.Polygon
                    try:
                        # multiple panel polygons
                        check = polygons[1].Position
                        print('inside multiple panel polygons')
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
                        panel_polygon.save(using=DB)

                        # converts bounds to vertices
                        northwest = PanelPosition()
                        northwest.panel_polygon = panel_polygon
                        northwest.lat = str(north)
                        northwest.lon = str(west)
                        northwest.save(using=DB)

                        northeast = PanelPosition()
                        northeast.panel_polygon = panel_polygon
                        northeast.lat = str(north)
                        northeast.lon = str(east)
                        northeast.save(using=DB)

                        southeast = PanelPosition()
                        southeast.panel_polygon = panel_polygon
                        southeast.lat = str(south)
                        southeast.lon = str(east)
                        southeast.save(using=DB)

                        southwest = PanelPosition()
                        southwest.panel_polygon = panel_polygon
                        southwest.lat = str(south)
                        southwest.lon = str(west)
                        southwest.save(using=DB)
                        print('--------- multi polygon panel, saved')

                    except:
                        try:
                            # single panel polygon
                            check = polygons.Position
                            print('inside single panel polygon')
                            panel_polygon = PanelPolygon()
                            panel_polygon.panel = panel
                            panel_polygon.save(using=DB)

                            positions = pan.Polygon.Position
                            for p in positions:
                                panel_position = PanelPosition()
                                panel_position.panel_polygon = panel_polygon
                                panel_position.lat = p['latitude']
                                panel_position.lon = p['longitude']
                                panel_position.save(using=DB)
                            print('--------- single polygon panel, saved')
                        except:
                            pass
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
                notice.save(using=DB)
                print('--------- notice: ' + notice.number + ', saved')
        except:
            pass

        if min > 45_000_000:
            chart.max_scale_category = 'undefined'
        else:
            chart.max_scale_category = utils.calculate_scale_category(min)
        chart.save(using=DB)
        print('chart.max_scale_category: ' + chart.max_scale_category)

    # sets import process finished flag to true
    catalogue.ready = True
    catalogue.save(using=DB)
    print('catalogue ready set to True')
