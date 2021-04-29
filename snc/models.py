from django.db import models
from django.utils import timezone

from pricecheck.const import *


class Catalogue(models.Model):
    file_identifier = models.CharField(max_length=50, default='')
    organisation_name = models.CharField(max_length=200, default='')
    fax = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    deliveryPoint = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=50, default='')
    administrative_area = models.CharField(max_length=50, default='')
    postal_code = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    date =  models.DateField(default=None, blank=True)
    expired = models.BooleanField(default=False)
    ready = models.BooleanField(default=False)


    def __str__(self):
        return self.file_identifier



class Chart(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, default=1)
    number = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=500, default='')
    scale = models.CharField(max_length=50, default='')
    folio = models.CharField(max_length=50, default='')
    last_nm_number = models.CharField(max_length=50, default='')
    last_nm_date = models.CharField(max_length=50, default='')
    cat_number = models.CharField(max_length=50, default='')
    int_number = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')
    status_date = models.DateField(default=None, blank=True)
    new_edition_date = models.DateField(default=None, blank=True)
    import_date = models.DateTimeField(default=None, blank=True)
    chart_scale_category = models.CharField(max_length=50, default='')
    max_scale_category = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.number + ', ' + self.title


class Panel(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE, default=1)
    panel_id = models.CharField(max_length=50, default='')
    area = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=500, default='')
    scale = models.CharField(max_length=50, default='')
    panel_scale_category = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.panel_id + ', ' + self.scale


class ChartPolygon(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=50, default='chart')

    def __str__(self):
        return self.type + ' polygon'


class PanelPolygon(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=50, default='panel')

    def __str__(self):
        return self.type + ' polygon'


class ChartPosition(models.Model):
    chart_polygon = models.ForeignKey(ChartPolygon, on_delete=models.CASCADE, default=1)
    lat = models.CharField(max_length=50, default='')
    lon = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.lat + ', ' + self.lon


class PanelPosition(models.Model):
    panel_polygon = models.ForeignKey(PanelPolygon, on_delete=models.CASCADE, default=1)
    lat = models.CharField(max_length=50, default='')
    lon = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.lat + ', ' + self.lon


class Notice(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE, default=1)
    year = models.CharField(max_length=50, default='')
    week = models.CharField(max_length=50, default='')
    number = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.year + ', ' + self.week + ' / ' + self.number


# ----------- ready made html with charts ------------

class Geojson(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, default=1)
    cat_id = models.CharField(max_length=50,default='')
    scale_range = models.CharField(max_length=500, default='')
    chart_range = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')
    json = models.TextField(max_length=5000000, default='no_data')
    chart_number = models.CharField(max_length=50, default='')
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.cat_id + ', ' + self.scale_range + ', charts number' + self.chart_number


class GeojsonCHS(models.Model):
    import_date = models.DateTimeField(default=None, blank=True)
    json_scale_1 = models.TextField(max_length=5000000, default='no_data')
    json_scale_2 = models.TextField(max_length=5000000, default='no_data')
    json_scale_3 = models.TextField(max_length=5000000, default='no_data')
    json_scale_4 = models.TextField(max_length=5000000, default='no_data')
    json_scale_5 = models.TextField(max_length=5000000, default='no_data')
    json_scale_all = models.TextField(max_length=5000000, default='no_data')
    type = models.CharField(max_length=50, default='')
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.id




