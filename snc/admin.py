from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Catalogue
from .models import Chart
from .models import Notice
from .models import ChartPolygon
from .models import ChartPosition
from .models import Panel
from .models import PanelPolygon
from .models import PanelPosition
from snc.const import *


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = DB_SNC

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(Catalogue, MultiDBModelAdmin)
admin.site.register(Chart, MultiDBModelAdmin)
admin.site.register(Notice, MultiDBModelAdmin)
admin.site.register(ChartPolygon, MultiDBModelAdmin)
admin.site.register(ChartPosition, MultiDBModelAdmin)
admin.site.register(Panel, MultiDBModelAdmin)
admin.site.register(PanelPolygon, MultiDBModelAdmin)
admin.site.register(PanelPosition, MultiDBModelAdmin)
