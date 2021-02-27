import django
django.setup()

import untangle
import xmltodict

import snc.catalogue, snc.chart, snc.notice, snc.panel, snc.point
from snc.const import *


# untangle ------------------------------------------------------------------
obj = untangle.parse(SNC_CATALOGUE_FILE)

#print(obj.UKHOCatalogueFile.BaseFileMetadata.MD_FileIdentifier.cdata)

#print(obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart[0].ShortName.cdata)

print('snc:')

snc_list = obj.UKHOCatalogueFile.Products.Paper.StandardNavigationChart
print(len(snc_list))

snc_slice = snc_list[3500:]
print(len(snc_slice))


for item in snc_list:
    # print(item.ShortName.cdata)
    # print(item.Metadata.DatasetTitle.cdata)
    # print(item.Metadata.Scale.cdata)
    # print(item.Metadata.GeographicLimit.Polygon)


    # pos = item.Metadata.GeographicLimit.Polygon.Position
    # for p in pos:
    #     print(p['latitude'] + ', ' + p['longitude'])

    try:
        boundbox = item.Metadata.GeographicLimit.BoundingBox
        print(item.ShortName.cdata)
        print(boundbox.NorthLimit.cdata)
    except:
        pass

















# ---------------------------------------------------------------------------


# xmltodict ------------------------------------------------------------------



# ---------------------------------------------------------------------------





