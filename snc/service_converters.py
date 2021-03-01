from snc.models import *
from snc.const import *
from snc.catalogue import *
from snc.chart import *
from snc.polygon import *
from snc.notice import *
from snc.panel import *
from snc.position import *



def chartDB_2_chartDTO(chartDB):
    chartDTO = ChartDTO()
    chartDTO.number = chartDB.number
    chartDTO.title = chartDB.title
    chartDTO.scale = chartDB.scale
    chartDTO.folio = chartDB.folio
    chartDTO.cat_number = chartDB.cat_number
    chartDTO.int_number = chartDB.int_number
    chartDTO.status =chartDB.status
    chartDTO.status_date = chartDB.status_date
    chartDTO.new_edition_date = chartDB.new_edition_date
    chartDTO.import_date = chartDB.import_date

    chart_polygonsDB = chartDB.chartpolygon_set.all()
    chartDTO.polygons = chart_polygonsDB_2_polygonsDTO(chart_polygonsDB)

    panelsDB = chartDB.panel_set.all()
    chartDTO.panels = panelsDB_2_panelsDTO(panelsDB)

    noticesDB = chartDB.notice_set.all()
    chartDTO.notices = noticedDB_2_noticesDTO(noticesDB)

    return chartDTO


def noticedDB_2_noticesDTO(noticesDB):
    noticesDTO = []
    if noticesDB != '':
        for noticeDB in noticesDB:
            noticeDTO = NoticeDTO
            noticeDTO.year = noticeDB.year
            noticeDTO.week = noticeDB.week
            noticeDTO.number = noticeDB.number
            noticeDTO.type = noticeDB.type
            noticesDTO.append(noticeDTO)
    return noticesDTO


def panelsDB_2_panelsDTO(panelsDB):
    panelsDTO = []
    for panelDB in panelsDB:
        panelDTO = PanelDTO
        panelDTO.panel_id = panelDB.panel_id
        panelDTO.area = panelDB.area
        panelDTO.name = panelDB.name
        panelDTO.scale = panelDB.scale
        polygonsDB = panelDB.panelpolygon_set.all()
        panelDTO.polygons = panel_polygonsDB_2_polygonsDTO(polygonsDB)
        panelsDTO.append(panelDTO)
    return panelsDTO





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
    return positionsDTO



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
    return positionsDTO




























