from snc.chart import *
from snc.polygon import *
from snc.notice import *
from snc.panel import *
from snc.position import *
from snc.models import *
from snc.const import *


def calculate_polygon_centre(polygon):
    positions = polygon.positions
    polyCentre = calculateCentreFromCoords(positions)
    return polyCentre


# Used for placing a label (chart's number)
def calculate_polygon_bottom_left_inside(polygon):
    latitudes = [float(x.lat) for x in polygon.positions]
    longitudes = [float(x.lon) for x in polygon.positions]

    latMax = findMax(latitudes)
    latMin = findMin(latitudes)
    lngMax = findMax(longitudes)
    lngMin = findMin(longitudes)

    # Google Maps Label Markers have the insetion point below the text
    # so no vertical (latitude) adjustment is not needed
    bottomLeftLat = latMin

    # This formula is a compromise: it will still overlap the chart's
    # boundry when zoomed out more than a few levels from the initial zoom level
    bottomLeftLng = lngMin + (lngMax - lngMin) * 0.05

    position = PositionDTO()
    position.lat = bottomLeftLat
    position.lon = bottomLeftLng

    return position


# Charts may have many polygons (panels). This method calculates
# the centre of all of them (which may not be inside any of the polygons).
def calculateChartCentre(chart):
    polyCentreList = []
    polygonList = chart.polygons
    for panel in chart.panels:
        polygonList.append(panel.polygons)
    for poly in polygonList:
        positions = poly.positions
        polyCentre = calculateCentreFromCoords(positions)
        polyCentreList.append(polyCentre)

    chartCentre = calculateCentreFromCoords(polyCentreList)
    return chartCentre


def calculateCentreFromCoords(positions):
    latitudes = []
    longitudes = []
    for pos in positions:
        latitudes.append(pos.lat)
        longitudes.append(pos.lon)

    latMax = findMax(latitudes)
    latMin = findMin(latitudes)
    lngMax = findMax(longitudes)
    lngMin = findMin(longitudes)

    middleLat = (latMax + latMin) / 2
    middleLng = (lngMax + lngMin) / 2

    position = PositionDTO()
    position.lat = middleLat
    position.lon = middleLng

    return position


# (-)180 degrees is the maximum (minimum) value for Longitude.
# It is (-)90 for Latitude but used the same for both for clarity
# (does not make any difference in this case).
def findMax(list):
    max = -180
    for d in list:
        if max < d:
            max = d
    return max


def findMin(list):
    min = 180
    for d in list:
        if min > d:
            min = d
    return min
