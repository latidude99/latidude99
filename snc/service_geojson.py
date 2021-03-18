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


# @range - list of scale range constants defined in const.py (SCALE_ALL_TEXT, SCALE_1_TEXT etc.)
def generate_geojson_and_save_db(range):
    catalogue = repo.get_latest_catalogue()
    geojson = Geojson()
    chartsDB = []

    for scale in range:
        if scale == SCALE_ALL_TEXT:
            chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue.id)
            geojson.scale_range = scale
        else:
            chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=scale)
            geojson.scale_range = scale

        charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
        json = generate_geojson(charts)

        geojson.json = json
        geojson.catalogue = catalogue
        geojson.cat_id = catalogue.id
        geojson.ready = True
        geojson.save(using='snc')

    return 'generated and saved in DB geojson for charts: ' + ', '.join(range)



def generate_geojson(charts):
    features = []
    invalid_charts = []
    invalid_panels = []

    for chart in charts:

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
                                 "chart_scale": f'{chart.scale:,}',
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
            print('polygon geometry added for ' + chart.number)
        else:
            invalid_charts.append(chart.number)


        for panel in chart.panels:
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
                                     "panel_scale": f'{panel.scale:,}',
                                     "polygons": len(panel.polygons),
                                     "set_zIndex": True,
                                     "zIndex": panel.zindex,
                                     "color": "green",
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

    # with open(SNC_GEOJSON_FILE, 'w') as f:
    #     dump(feature_collection, f)

    print(geo_str)

    return geo_str






























