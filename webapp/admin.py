from django.contrib import admin
from .models import Webapp
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Webapp)

class ViewAdmin(ImportExportModelAdmin):
	pass

class AdjustDataAdmin(admin.ModelAdmin):
	list_display = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',)
	list_filter = ('channel', 'country', 'os',)