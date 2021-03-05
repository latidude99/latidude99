#import django
#django.setup()

from django.shortcuts import render
from django.template.loader import render_to_string

import snc.service as service
from snc.const import *


def charts_1_to_html_and_save(chart_scale, file):
    context= ''
    if chart_scale == SCALE_1_TEXT:
        context = service.get_SCALE1_charts_context()
    elif chart_scale == SCALE_2_TEXT:
        context = service.get_SCALE2_charts_context()
    elif chart_scale == SCALE_3_TEXT:
        context = service.get_SCALE3_charts_context()
    elif chart_scale == SCALE_4_TEXT:
        context = service.get_SCALE4_charts_context()
    elif chart_scale == SCALE_5_TEXT:
        context = service.get_SCALE5_charts_context()
    elif chart_scale == SCALE_6_TEXT:
        context = service.get_SCALE6_charts_context()
    elif chart_scale == SCALE_7_TEXT:
        context = service.get_SCALE7_charts_context()

    if context != '':
        html_str = render_to_string('snc/index.html', context)
        f = open(file, 'w+')
        f.write(html_str)
        f.close()
        print('---- render to html ok ----')
    else:
        print('no context')
    #print(html_str)
    return 'render to html ok'


#print(charts_1_to_html_and_save(SCALE_2_TEXT, SNC_SCALE_2_HTML))








