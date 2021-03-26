#import django
#django.setup()

import untangle
#import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.position
from snc.models import *
from snc.const import *
import snc.service_parse as service_parse
import snc.service_converters as service_converters


def get_latest_catalogue():
    catalogue = ''
    catalogues = Catalogue.objects.using('snc').all()
    for c in reversed(catalogues):
        print(c.id)
        if c.ready:
            catalogue = c
            break
    return catalogue


# ------------------------- geojson ---------------------------------
def find_geojson_single(num):
    catalogue = get_latest_catalogue()
    geojson = Geojson.objects.using('snc').filter(cat_id=catalogue.id, chart_number=num).latest("id")
    return geojson


def find_geojson_multiple(nums):
    catalogue = get_latest_catalogue()

    comma = ','
    json_start = '{"type": "FeatureCollection", "features": ['  # 42 chars
    json_end = ']}'  # 2 chars

    json = json_start
    for num in nums:
        if Geojson.objects.using('snc').filter(cat_id=catalogue.id, chart_number=num).exists():
            #geojson_single = Geojson.objects.using('snc').filter(cat_id=catalogue.id, chart_number=num).latest("id")
            geojson_single = Geojson.objects.using('snc').filter(chart_number=num).latest("id")
            json = json + geojson_single.json[43:-2] + comma
        print('added' + str(num))
    json = json[:-1] + json_end  # removing comma after last feature
    return json


def find_geojson_scale_range_all_split_scales(catalogue):
    geojson = {}
    # catalogue = get_latest_catalogue()
    #geojson = Geojson.objects.using('snc').filter(cat_id=catalogue.id, scale_range=scale_range).latest("id")

    geojson['scale1'] = Geojson.objects.using('snc').filter(scale_range=SCALE_1_TEXT).latest("id").json
    geojson['scale2'] = Geojson.objects.using('snc').filter(scale_range=SCALE_2_TEXT).latest("id").json
    geojson['scale3'] = Geojson.objects.using('snc').filter(scale_range=SCALE_3_TEXT).latest("id").json
    geojson['scale4'] = Geojson.objects.using('snc').filter(scale_range=SCALE_4_TEXT).latest("id").json
    geojson['scale5'] = Geojson.objects.using('snc').filter(scale_range=SCALE_5_TEXT).latest("id").json
    geojson['scale6'] = Geojson.objects.using('snc').filter(scale_range=SCALE_6_TEXT).latest("id").json
    geojson['scale7'] = Geojson.objects.using('snc').filter(scale_range=SCALE_7_TEXT).latest("id").json

    return geojson


# takes single scale range as string
def find_geojson_scale_range_single(catalogue, scale_range):
    # catalogue = get_latest_catalogue()
    #geojson = Geojson.objects.using('snc').filter(cat_id=catalogue.id, scale_range=scale_range).latest("id")
    geojson = Geojson.objects.using('snc').filter(scale_range=scale_range).latest("id")
    return geojson


# takes multiple scale ranges as list of strings
def find_geojson_scale_range_multiple(catalogue, scale_ranges):
    # catalogue = get_latest_catalogue()

    comma = ','
    json_start = '{"type": "FeatureCollection", "features": ['  # 42 chars
    json_end = ']}'  # 2 chars

    json = json_start
    for scale_range in scale_ranges:
        if Geojson.objects.using('snc').filter(cat_id=catalogue.id, scale_range=scale_range).exists():
            # geojson_single = Geojson.objects.using('snc').filter(cat_id=catalogue.id, scale_range=scale_range).latest("id")
            geojson_single = Geojson.objects.using('snc').filter(scale_range=scale_range).latest("id")
            json = json + geojson_single.json[43:-2] + comma
        print('added' + str(scale_range))
    json = json[:-1] + json_end  # removing comma after last feature
    return json


# ------------------------- chartDTO ---------------------------------
def find_chart(num):
    catalogue = get_latest_catalogue()
    chart = catalogue.chart_set.filter(number=num)
    return chart

def find_charts(nums):
    charts = []
    catalogueDB = get_latest_catalogue()
    # catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    if len(nums) == 0:
        nums = range(1, 3)
    for num in nums:
        if catalogueDB.chart_set.filter(number=num).exists():
            chartDB = catalogueDB.chart_set.get(number=num)
            chart = service_converters.chartDB_2_chartDTO(chartDB)
            charts.append(chart)
    return charts



def find_charts_all():
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id)
    return charts


def find_charts_SCALE_1(): # 24 charts
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_1_TEXT)
    return charts


def find_charts_SCALE_2(): # 875 charts
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_2_TEXT)
    return charts


def find_charts_SCALE_3(): # 270 charts
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_3_TEXT)
    return charts


def find_charts_SCALE_4(): # 31 charts
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_4_TEXT)
    return charts


def find_charts_SCALE_5(): # 10 charts
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_5_TEXT)
    return charts


def find_charts_SCALE_6(): #
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_6_TEXT)
    return charts


def find_charts_SCALE_7():
    catalogue = get_latest_catalogue()
    charts = Chart.objects.using('snc').filter(catalogue=catalogue.id, max_scale_category=SCALE_7_TEXT)
    return charts



# adds scale category to imported charts that are missing it
def add_scale_category():
    catalogue = get_latest_catalogue()

    if catalogue != '':
        chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue.id)

        for ch in chartsDB:
            ch.max_scale_category = get_scale_category(ch)
            ch.save(using='snc')
            print('chart ' + ch.number + ', scale category added')


def get_scale_category(chart):
    min = 100000000
    if chart.scale != '' and int(chart.scale.strip()) < min:
        min = int(chart.scale.strip())
    panels = chart.panel_set.all()
    if len(panels) > 0:
        for p in panels:
            if p.scale != '' and int(p.scale.strip()) < min:
                min = int(p.scale.strip())
    return calculate_scale_category(min)


def calculate_scale_category(scale):
    category = ''
    if scale < SCALE_1:
        category = SCALE_1_TEXT
    elif scale < SCALE_2:
        category = SCALE_2_TEXT
    elif scale < SCALE_2:
        category = SCALE_2_TEXT
    elif scale < SCALE_3:
        category = SCALE_3_TEXT
    elif scale < SCALE_4:
        category = SCALE_4_TEXT
    elif scale < SCALE_5:
        category = SCALE_5_TEXT
    elif scale < SCALE_6:
        category = SCALE_6_TEXT
    elif scale > SCALE_6:
        category = SCALE_7_TEXT
    return category


def print_chart_detail():
    catalogue = get_latest_catalogue()

    if catalogue != '':
        chartsDB = Chart.objects.using('snc').filter(catalogue=catalogue.id, number='1006')

        for ch in chartsDB:
            chart = service_converters.chartDB_2_chartDTO(ch)

            print('\n')
            print('chart number----------------')
            print(chart.number)
            print(chart.title)
            print(chart.scale)
            print(chart.status)
            print(chart.status_date)
            print(chart.folio)
            print(chart.cat_number)

            print('chart polygons----------------')
            print(chart.polygons)
            if len(chart.polygons) > 0:
                print(len(chart.polygons))
                print(chart.polygons[0].positions[0].lat)
                print(chart.polygons[0].positions[0].lon)

            print('panels----------------')
            print(chart.panels)
            if len(chart.panels) > 0:
                print(chart.panels[0].polygons)
                print(chart.panels[0].polygons[0].positions[0].lat)
                print(chart.panels[0].polygons[0].positions[0].lon)

            print('notices----------------')
            print(chart.notices)
            if len(chart.notices) > 0:
                print(chart.notices[0].week)

    else:
        print('no catalogue loaded')











