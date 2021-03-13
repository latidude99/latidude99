#import django
#django.setup()

import random
import string
from snc.text import *
from snc.const import *
import snc.repository as repo
import snc.service_converters as service_converters
import snc.utils as utils
from snc.chart import *
from snc.position import *

def generate_geojson(charts):
    start = '{ \n' \
        '  "type": "FeatureCollection",\n' \
        '  "features": [\n'
    chart = ChartDTO()

    for chart in charts:
        if len(chart.polygons) > 0:
            poly_type = 'chart'
            if chart.chart_centre != '':
                # pos = PositionDTO
                pos_c = chart.chart_centre
                centre = '[' + pos_c.lat + ', ' + pos_c.lon + ']'
            else:
                centre = ''
            if chart.label_position != '':
                # pos = PositionDTO
                pos_l = chart.label_position
                label_position = '[' + pos_l.lat + ', ' + pos_l.lon + ']'
            else:
                label_position = ''

            middle = '    {\n' \
        '      "type": "Feature",\n' \
        '      "properties": {\n' \
        '        "polyType": "' + poly_type + '",\n' \
        '        "number": "' + chart.number + '",\n' \
        '        "title": "' + chart.title + '",\n' \
        '        "scale": "' + chart.scale + '",\n' \
        '        "edition": "' + chart.new_edition_date + '"\n' \
        '        "lastNM": "' + chart.last_nm_number + '"\n' \
        '        "lastNMdate": "' + chart.last_nm_date + '"\n' \
        '        "maxScaleCategory": "' + chart.max_scale_category + '"\n' \
        '        "zoomMin": "' + chart.zoom_min + '"\n' \
        '        "zoomMax": "' + chart.zoom_max + '"\n' \
        '        "chartCentre": "' + centre + '"\n' \
        '        "colour": "' + chart.colour + '"\n' \
        '        "zindex": "' + chart.zindex + '"\n' \
        '        "labelPosition": "' + label_position + '"\n' \
        '      },\n' \
        '      "geometry": {\n' \
        '        "type": "Polygon",\n'
        if len(chart.polygons) > 0:
            middle_poly = '        "coordinates": [\n' \
        '          [\n' \
        '            [48.16667, -13.78665],\n' \
        '            [62.83405, -13.78665 ],\n' \
        '            [62.83405, 3.41228],\n' \
        '            [48.16667, 3.41228],\n' \
        '            [48.16667, -13.78665]\n' \
        '          ]\n'
        else:
            middle_poly = '        "coordinates": []\n'

        middle_end = '        ]\n' \
        '      }\n' \
        '    }'

        if len(chart.panels) > 0:
            poly_type = 'panel'

            for panel in chart.panels:
                if panel.panel_centre != '':
                    pos_cp = panel.panel_centre
                    panel_centre = '[' + pos_cp.lat + ', ' + pos_cp.lon + ']'
                else:
                    panel_centre = ''
                if panel.label_position != '':
                    pos_lp = panel.label_position
                    panel_label_position = '[' + pos_lp.lat + ', ' + pos_lp.lon + ']'
                else:
                    panel_label_position = ''
                middle = '    {\n' \
                         '      "type": "Feature",\n' \
                         '      "properties": {\n' \
                         '        "polyType": "' + poly_type + '",\n' \
                         '        "number": "' + chart.number + '",\n' \
                         '        "panelId": "' + panel.panel_id + '",\n' \
                         '        "title": "' + panel.name + '",\n' \
                         '        "scale": "' + panel.scale + '",\n' \
                         '        "edition": "' + chart.new_edition_date + '"\n' \
                         '        "lastNM": "' + chart.last_nm_number + '"\n' \
                         '        "lastNMdate": "' + chart.last_nm_date + '"\n' \
                         '        "panelCentre": "' + panel_centre + '"\n' \
                         '        "colour": "' + chart.colour + '"\n' \
                         '        "zindex": "' + chart.zindex + '"\n' \
                         '        "labelPosition": "' + panel_label_position + '"\n' \
                         '      },\n' \
                         '      "geometry": {\n' \
                         '        "type": "Polygon",\n' \
                         '        "coordinates": [\n' \
                         '          [\n' \
                         '            [48.16667, -13.78665],\n' \
                         '            [62.83405, -13.78665 ],\n' \
                         '            [62.83405, 3.41228],\n' \
                         '            [48.16667, 3.41228],\n' \
                         '            [48.16667, -13.78665]\n' \
                         '          ]\n' \
                         '        ]\n' \
                         '      }\n' \
                         '    }'

        comma = ',\n'
        end = '\n  ]\n' \
    '}\n '
    out_string = start + middle + comma + middle + end
    return text





'''

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "letter": "G",
        "color": "blue",
        "rank": "7",
        "ascii": "71"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [48.16667, -13.78665],

				[62.83405, -13.78665 ],

                [62.83405, 3.41228],

                [48.16667, 3.41228],

                [48.16667, -13.78665]
          ]
        ]
      }
    },
  ]
}    
'''





