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
import datetime as dt

def generate_geojson(charts):
    chart_start_str = '{ \n' \
        '  "type": "FeatureCollection",\n' \
        '  "features": [\n'
    chart = ChartDTO()

    total_out_string = ''
    chart_out_string= ''
    for chart in charts:
       # print(chart.polygons[0].positions)
        chart_out_string = ''
        chart_middle_str = ''
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
                label_position = '[' + str(pos_l.lat) + ', ' + str(pos_l.lon) + ']'
            else:
                label_position = ''

            chart_middle_str = '    {\n' \
        '      "type": "Feature",\n' \
        '      "properties": {\n' \
        '        "polyType": "' + poly_type + '",\n' \
        '        "number": "' + str(chart.number) + '",\n' \
        '        "title": "' + chart.title + '",\n' \
        '        "scale": "' + str(chart.scale) + '",\n' \
        '        "edition": "' + chart.new_edition_date.strftime('%d %B %Y') + '"\n' \
        '        "lastNM": "' + chart.last_nm_number + '"\n' \
        '        "lastNMdate": "' + chart.last_nm_date + '"\n' \
        '        "maxScaleCategory": "' + chart.max_scale_category + '"\n' \
        '        "zoomMin": "' + str(chart.zoom_min) + '"\n' \
        '        "zoomMax": "' + str(chart.zoom_max) + '"\n' \
        '        "chartCentre": "' + centre + '"\n' \
        '        "colour": "' + chart.colour + '"\n' \
        '        "zindex": "' + str(chart.zindex) + '"\n' \
        '        "labelPosition": "' + label_position + '"\n' \
        '      },\n' \
        '      "geometry": {\n' \
        '        "type": "Polygon",\n'
        if len(chart.polygons) > 0:
            chart_middle_poly_str = '        "coordinates": [\n'
            for poly in chart.polygons:
                '          [\n'
                for pos in poly.positions:
                    '['+ str(pos.lat) + ', ' + str(pos.lon) + '], ' \
                ',\n' \
            '          ]\n'
        else:
            chart_middle_poly_str = '        "coordinates": []\n'

        chart_middle_end_str = '        ]\n' \
        '      }\n' \
        '    }'

        panels_str= ''
        middle_str = ''
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
                    panel_label_position = '[' + str(pos_lp.lat) + ', ' + str(pos_lp.lon) + ']'
                else:
                    panel_label_position = ''
                middle_str = '    {\n' \
                         '      "type": "Feature",\n' \
                         '      "properties": {\n' \
                         '        "polyType": "' + poly_type + '",\n' \
                         '        "number": "' + str(chart.number) + '",\n' \
                         '        "panelId": "' + str(panel.panel_id) + '",\n' \
                         '        "title": "' + panel.name + '",\n' \
                         '        "scale": "' + str(panel.scale) + '",\n' \
                         '        "edition": "' + chart.new_edition_date.strftime('%d %B %Y') + '"\n' \
                         '        "lastNM": "' + chart.last_nm_number + '"\n' \
                         '        "lastNMdate": "' + chart.last_nm_date + '"\n' \
                         '        "panelCentre": "' + panel_centre + '"\n' \
                         '        "colour": "' + chart.colour + '"\n' \
                         '        "zindex": "' + str(chart.zindex) + '"\n' \
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

        comma_str = ',\n'
        end_str = '\n  ]\n'
        chart_out_string = chart_start_str + chart_middle_str + chart_middle_poly_str + comma_str + middle_str + end_str
        total_out_string = total_out_string + chart_out_string

    # '}\n '
    return total_out_string





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





