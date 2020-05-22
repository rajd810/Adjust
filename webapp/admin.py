from django.contrib import admin
from .models import Webapp
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Webapp)

class ViewAdmin(ImportExportModelAdmin):
	pass