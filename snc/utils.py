#import django
#django.setup()

import untangle
#import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.position
from snc.models import *
from snc.const import *
import snc.service_parse as service_parse
import snc.service_converters as service_converters
import random


def get_latest_catalogue():
    catalogue = ''
    while True:
        catalogue = Catalogue.objects.using('snc').latest('date')
        if catalogue.ready:
            break
    return catalogue


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


def get_colour():
    colours = ["#0033cc", "#008080", "#996633", "#990033", "#006666", "#73264d", "#660066", "#000099",
               "#004d00", "#800000", "#006622", "#66194d", "#24478f", "#806000", "#260033", "#992600", "#003300"]
    return random.choice(colours)


















