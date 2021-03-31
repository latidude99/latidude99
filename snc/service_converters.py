from snc.models import *
from snc.const import *
from snc.catalogue import *
from snc.chart import *
from snc.polygon import *
from snc.notice import *
from snc.panel import *
from snc.position import *
from snc.utils import *
from snc.utils_chart_centre import *
import datetime as dt


def catalogueDB_2_catalogueDTO(db):
    dto = CatalogueDTO()
    dto.file_identifier = db.file_identifier
    dto.organisation_name = db.organisation_name
    dto.fax = db.fax
    dto.phone = db.phone
    dto.delivery_point = db.deliveryPoint
    dto.city = db.city
    dto.administrative_area = db.administrative_area
    dto.postal_code = db.postal_code
    dto.country = db.country
    dto.email = db.email
    dto.date = db.date  # .strftime('%d %B %Y')
    dto.charts_count = db.chart_set.all().count()
    return dto


def chartsDB_2_chartsDTO(chartsDB):
    charts = []
    print(chartsDB)
    for chartDB in chartsDB:
        if chartDB != None:
            chart = chartDB_2_chartDTO(chartDB)
            charts.append(chart)
    return charts


def chartsDB_2_chartsDTO_except8XXX(chartsDB):
    charts = []
    print(chartsDB)
    for chartDB in chartsDB:
        try:
            if (int(chartDB.number) > 7999) & (int(chartDB.number) < 9000): # port approaches chart numbers
                chart = chartDB_2_chartDTO(chartDB)
                charts.append(chart)
        except:
            pass
    return charts


def chartDB_2_chartDTO(chartDB):
    chartDTO = ChartDTO()
    chartDTO.catalogue_id = chartDB.catalogue.date.strftime('%d %b %Y') # chartDB.catalogue.file_identifier + ', ' +
    chartDTO.number = chartDB.number
    chartDTO.title = chartDB.title
    if chartDB.scale != '':
        chartDTO.scale = int(chartDB.scale)
        chartDTO.zindex = int(1000000000 / int(chartDB.scale))  # zoom['max']
        #print(int(100000000 / int(chartDB.scale)))
        print('chartDTO.zindex ' + str(chartDTO.zindex))
    chartDTO.folio = chartDB.folio
    chartDTO.cat_number = chartDB.cat_number
    chartDTO.int_number = chartDB.int_number
    chartDTO.status = chartDB.status
    chartDTO.status_date = chartDB.status_date
    chartDTO.new_edition_date = chartDB.new_edition_date
    chartDTO.import_date = chartDB.import_date
    chartDTO.last_nm_number = chartDB.last_nm_number
    chartDTO.last_nm_date = chartDB.last_nm_date

    # AFAIK only one main chart, could change in future
    chart_polygonsDB = chartDB.chartpolygon_set.all()
    chartDTO.polygons = chart_polygonsDB_2_polygonsDTO(chart_polygonsDB)

    panelsDB = chartDB.panel_set.all()
    chartDTO.panels = panelsDB_2_panelsDTO(panelsDB)

    if len(chartDTO.polygons) == 0 and len(chartDTO.panels) == 1:
        chartDTO.polygons = chartDTO.panels[0].polygons
        chartDTO.scale = chartDTO.panels[0].scale
        chartDTO.panels = []

    noticesDB = chartDB.notice_set.all()
    chartDTO.notices = noticesDB_2_noticesDTO(noticesDB)
    chartDTO.notices.reverse()  # newest first

    chartDTO.max_scale_category = chartDB.max_scale_category
    scale = ''
    if chartDB.scale != '':
        scale = chartDB.scale
    elif len(panelsDB) > 0:
        scale = panelsDB[0].scale
    if scale != '':
        # sets display zoom levels
        zoom = calculateZoomMaxMin(int(scale.strip()))
        zoom_const = getZoomMaxMin()
        chartDTO.zoom_min = zoom_const['min']
        chartDTO.zoom_max = zoom_const['max']

    if len(chartDTO.polygons) > 0:
        chartDTO.label_position = calculate_polygon_bottom_left_inside(chartDTO.polygons[0])
    chartDTO.colour = CHART_COLOUR

    print('chart ' + chartDTO.number + ' converted from DB to DTO')
    return chartDTO


# not used for the time being
def get_chart_polys_formatted(polygonsDB):
    polys = []
    if len(polygonsDB) > 0:
        for polygonDB in polygonsDB:
            poly = []
            positionsDB = polygonDB.chartposition_set.all()
            for pos in positionsDB:
                position = 'new google.maps.LatLng(' + pos.lat + ', ' + pos.lon + ')'
                poly.append(position)
            polys.append(poly)
    return polys


def noticesDB_2_noticesDTO(noticesDB):
    noticesDTO = []
    if noticesDB != '':
        for noticeDB in noticesDB:
            noticeDTO = NoticeDTO()
            noticeDTO.year = noticeDB.year
            noticeDTO.week = noticeDB.week
            noticeDTO.number = noticeDB.number
            noticeDTO.type = noticeDB.type
            noticesDTO.append(noticeDTO)
    return noticesDTO


def panelsDB_2_panelsDTO(panelsDB):
    panelsDTO = []
    for panelDB in panelsDB:
        panelDTO = PanelDTO()
        panelDTO.panel_id = panelDB.panel_id
        panelDTO.area = panelDB.area
        panelDTO.name = panelDB.name
        if panelDB.scale != '':
            panelDTO.scale = int(panelDB.scale)
            zoom = calculateZoomMaxMin(int(panelDB.scale.strip()))
            panelDTO.zindex = int(1000000000 / int(panelDB.scale)) # zoom['max']
            print('panelDTO.zindex ' + str(panelDTO.zindex))
        polygonsDB = panelDB.panelpolygon_set.all()
        panelDTO.polygons = panel_polygonsDB_2_polygonsDTO(polygonsDB)
        if len(panelDTO.polygons) > 0:
            panelDTO.label_position = calculate_polygon_bottom_left_inside(panelDTO.polygons[0])
        panelDTO.colour = PANEL_COLOUR
        panelsDTO.append(panelDTO)
    return panelsDTO


def panel_polygonsDB_2_polygonsDTO(polygonsDB):
    polygonsDTO = []
    for polygonDB in polygonsDB:
        polygonDTO = PolygonDTO()
        positionsDB = polygonDB.panelposition_set.all()
        polygonDTO.positions = panel_positionsDB_2_positionsDTO(positionsDB)
        polygonsDTO.append(polygonDTO)
    return polygonsDTO


def panel_positionsDB_2_positionsDTO(positionsDB):
    positionsDTO = []
    for p in positionsDB:
        posDTO = PositionDTO()
        posDTO.lat = p.lat
        posDTO.lon = p.lon
        positionsDTO.append(posDTO)
    # closes polygons, necessary for Google Maps Data.Polygon (not necessary for Google Maps Polygon)
    if positionsDTO[0].lat != positionsDTO[-1].lat or positionsDTO[0].lon != positionsDTO[-1].lon:
        positionsDTO.append(positionsDTO[0])
    return positionsDTO


def chart_polygonsDB_2_polygonsDTO(polygonsDB):
    polygonsDTO = []
    for polygonDB in polygonsDB:
        polygonDTO = PolygonDTO()
        positionsDB = polygonDB.chartposition_set.all()
        polygonDTO.positions = chart_positionsDB_2_positionsDTO(positionsDB)
        polygonsDTO.append(polygonDTO)
    return polygonsDTO


def chart_positionsDB_2_positionsDTO(positionsDB):
    positionsDTO = []
    for p in positionsDB:
        posDTO = PositionDTO()
        posDTO.lat = p.lat
        posDTO.lon = p.lon
        positionsDTO.append(posDTO)
    # closes polygons, necessary for Google Maps Data.Polygon (not necessary for Google Maps Polygon)
    if positionsDTO[0].lat != positionsDTO[-1].lat or positionsDTO[0].lon != positionsDTO[-1].lon:
        positionsDTO.append(positionsDTO[0])
    return positionsDTO


def getZoomMaxMin():
    maxmin_levels = {}
    maxmin_levels['max'] = '22'
    maxmin_levels['min'] = '1'
    return maxmin_levels


def calculateZoomMaxMin(scale):
    maxmin_levels = {}
    if scale < 50_000_000 and scale > 20_000_000:
        maxmin_levels['max'] = '3'
        maxmin_levels['min'] = '1'
    elif scale < 20_000_001 and scale > 10_000_000:
        maxmin_levels['max'] = '3'
        maxmin_levels['min'] = '2'
    elif scale < 10_000_001 and scale > 5_000_000:
        maxmin_levels['max'] = '4'
        maxmin_levels['min'] = '2'
    elif scale < 5_000_001 and scale > 2_000_000:
        maxmin_levels['max'] = '5'
        maxmin_levels['min'] = '2'
    elif scale < 2_000_001 and scale > 1_000_000:
        maxmin_levels['max'] = '6'
        maxmin_levels['min'] = '3'
    elif scale < 1_000_001 and scale > 500_000:
        maxmin_levels['max'] = '7'
        maxmin_levels['min'] = '4'
    elif scale < 500_001 and scale > 300_000:
        maxmin_levels['max'] = '8'
        maxmin_levels['min'] = '5'
    elif scale < 300_001 and scale > 100_000:
        maxmin_levels['max'] = '10'
        maxmin_levels['min'] = '6'
    elif scale < 100_001 and scale > 80_000:
        maxmin_levels['max'] = '11'
        maxmin_levels['min'] = '7'
    elif scale < 80_001 and scale > 50_000:
        maxmin_levels['max'] = '12'
        maxmin_levels['min'] = '7'
    elif scale < 50_001 and scale > 30_000:
        maxmin_levels['max'] = '13'
        maxmin_levels['min'] = '8'
    elif scale < 30_001 and scale > 20_000:
        maxmin_levels['max'] = '22'
        maxmin_levels['min'] = '8'
    elif scale < 20_001 and scale > 10_000:
        maxmin_levels['max'] = '22'
        maxmin_levels['min'] = '9'
    elif scale < 10_001 and scale > 8_000:
        maxmin_levels['max'] = '22'
        maxmin_levels['min'] = '9'
    elif scale < 8_001 and scale > 5_000:
        maxmin_levels['max'] = '22'
        maxmin_levels['min'] = '9'
    elif scale < 5_001 and scale > 1_000:
        maxmin_levels['max'] = '22'
        maxmin_levels['min'] = '10'
    else:
        maxmin_levels['max'] = '5'
        maxmin_levels['min'] = '1'

    return maxmin_levels
