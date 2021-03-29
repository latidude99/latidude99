#import django
#django.setup()

import snc.service_converters as service_converters
import snc.repository as repo
from snc.models import *
from geojson import Point, Polygon, MultiPolygon, Feature, FeatureCollection, dump
import json
from snc.text import *
from snc.const import *
from snc.chart import *
from snc.position import *
import datetime as dt
import locale


def save_geojson_to_file(geojson, file):
    with open(file, 'w') as f:
        dump(geojson, f)
    return 'geojson saved to file'


# @range - list of chart numbers
def generate_geojson_and_save_db_single_charts(nums):
    catalogue = repo.get_latest_catalogue()
    processed = []

    if len(nums) == 0:
        chartsDB = catalogue.chart_set.all()
        for chartDB in chartsDB:
            chart = service_converters.chartDB_2_chartDTO(chartDB)
            gjson = generate_geojson([chart])

            geojson = Geojson()
            geojson.type = 'single'
            geojson.chart_number = chartDB.number
            geojson.json = gjson
            geojson.catalogue = catalogue
            geojson.cat_id = catalogue.id
            geojson.ready = True
            geojson.save(using='snc')
            processed.append(chartDB.number)

    else:
        for num in nums:
            if Chart.objects.using('snc').filter(catalogue=catalogue, number=num).exists():
                chartDB = Chart.objects.using('snc').get(catalogue=catalogue, number=num)
                print(chartDB)
                chart = service_converters.chartDB_2_chartDTO(chartDB)
                gjson = generate_geojson([chart])

                geojson = Geojson()
                geojson.type = 'single'
                geojson.chart_number = num
                geojson.json = gjson
                geojson.catalogue = catalogue
                geojson.cat_id = catalogue.id
                geojson.ready = True
                geojson.save(using='snc')
                processed.append(num)

    return 'generated and saved in DB geojson for charts: ' + str(range)


# @range - list of scale range constants defined in const.py (SCALE_ALL_TEXT, SCALE_1_TEXT etc.)
def generate_geojson_and_save_db(scale_range):
    catalogue = repo.get_latest_catalogue()

    chartsDB = []

    for scale in scale_range:
        geojson = Geojson()
        if scale == SCALE_ALL_TEXT:
            chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue) #.latest('id')
            geojson.scale_range = scale_range
        else:
            chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue, max_scale_category=scale) #.latest('id')
            geojson.scale_range = scale
            print(scale)

        charts = service_converters.chartsDB_2_chartsDTO(chartsDB)

        if len(charts) > 0:
            gjson = generate_geojson(charts)

            geojson.json = gjson
            geojson.catalogue = catalogue
            geojson.cat_id = catalogue.id
            geojson.ready = True
            geojson.save(using='snc')

    return 'generated and saved in DB geojson for charts: ' + ', '.join(scale_range)


def generate_geojson(charts):
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
    features = []
    invalid_charts = []
    invalid_panels = []

    for chart in charts:
        if chart.scale != '':
            chart_scale = f'{int(chart.scale):n}'
        else:
            chart_scale = ''

        geo_chart_polys = []
        for chart_poly in chart.polygons:
            geo_chart_poly = Polygon([[(float(x.lon), float(x.lat)) for x in chart_poly.positions]])
            geo_chart_polys.append(geo_chart_poly)
        chart_multi_poly = MultiPolygon(geo_chart_polys)
        # print(chart_multi_poly.is_valid)
        if chart_multi_poly.is_valid:
            features.append(Feature
                            (geometry=chart_multi_poly,
                             properties={
                                 "type": "chart",
                                 "catalogue_id": chart.catalogue_id,
                                 "chart_number": chart.number,
                                 "chart_title": chart.title,
                                 "chart_scale": chart_scale, # processed
                                 "edition": chart.new_edition_date.strftime('%d %B %Y'),
                                 "last_nm_number": chart.last_nm_number,
                                 "last_nm_date": chart.last_nm_date,
                                 "polygons": len(chart.polygons),
                                 "panels": len(chart.panels),
                                 "set_zIndex": True,
                                 "zIndex": chart.zindex,
                                 "color": "navy",
                                 "max_scale_category": chart.max_scale_category,
                             }))
            print('polygon geometry added for ' + chart.number + ', zindex = ' + str(chart.zindex))
        else:
            invalid_charts.append(chart.number)


        for panel in chart.panels:
            if panel.scale != '':
                panel_scale = f'{int(panel.scale):n}'
            else:
                panel_scale = ''

            geo_panel_polys = []
            for panel_poly in panel.polygons:
                geo_poly = Polygon([[(float(x.lon), float(x.lat)) for x in panel_poly.positions]])
                geo_panel_polys.append(geo_poly)
            panel_multi_poly = MultiPolygon(geo_panel_polys)
            # print(multi_poly.is_valid)
            if panel_multi_poly.is_valid:
                features.append(Feature
                                (geometry=panel_multi_poly,
                                 properties={
                                     "type": "panel",
                                     "catalogue_id": chart.catalogue_id,
                                     "chart_number": chart.number,
                                     "chart_title": chart.title,
                                     "panel_number": panel.panel_id,
                                     "panel_name": panel.name,
                                     "panel_scale": panel_scale, # processed
                                     "polygons": len(panel.polygons),
                                     "set_zIndex": True,
                                     "zIndex": panel.zindex,
                                     "color": "green",
                                     "max_scale_category": chart.max_scale_category,
                                 }))
                print('polygon geometry added for ' + chart.number)
            else:
                invalid_panels.append(chart.number + panel.panel_id)


    print('invalid polygons in charts:')
    print(invalid_charts)
    print('invalid polygons in panels:')
    print(invalid_panels)

    feature_collection = FeatureCollection(features)

    geo_str = json.dumps(feature_collection)
    #print(geo_str)

    return geo_str




























