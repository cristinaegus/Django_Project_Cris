from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    pass
