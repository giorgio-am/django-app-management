from django.contrib import admin

# Register your models here.
from django.apps import apps


# models = get_models()
#
# for model in models:
#     admin.site.register(model)
from django.apps import apps, AppConfig
from django.contrib import admin

from django.utils.html import format_html
from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
from .models import Kpi


admin.site.register(Kpi)
# admin.site.register(Derpartamentos)
# admin.site.register(Subdirecciones)
# admin.site.register(FichasProcesos)
@admin.register(Ley18834)
class Ley18834Admin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("ano", "establecimiento", "indicador", "meta", "numerador", "denominador", "resultado")

    # Let you to search with title name, release year and length of duration of movie
    search_fields = ['ano', 'establecimiento', 'indicador']
    # There will be a filter on release year
    list_filter = ['ano', 'establecimiento']

@admin.register(FichasProcesos)
class FichasProcesosAdmin(ExportActionMixin, admin.ModelAdmin):
    view_on_site = True
    def flujo_preview(self, obj):
        try:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;"/>',(obj.flujo.url))
        except:
            pass
    flujo_preview.allow_tags = True
    flujo_preview.short_description = 'Miniatura'

    def procesos_hijos(self, obj):
        return list(obj.hijos.all())

    list_display = ("nombre_proceso", "dpto_responsable", "subdirección", "alcance", "clasificación_interna", "madurez", "estado",'flujo_preview', 'flujo', 'procesos_hijos', 'macroproceso_padre')
    #readonly_fields = ('flujo',)

    # Let you to search with title name, release year and length of duration of movie// trabajo con __ por problemas con foreign key
    search_fields = ['nombre_proceso', 'dpto_responsable__id_dpto', 'subdirección__nombre_subdireccion', 'clasificación_interna__id_clasificación', 'estado__id_estado']
    # There will be a filter on release year
    list_filter = ['dpto_responsable',  'subdirección', 'clasificación_interna', 'estado', 'madurez' ]


@admin.register(Subprocesos)
class SubprocesosAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("id_subproceso", "nombre_subproceso", "proceso_padre")

    # Let you to search with title name, release year and length of duration of movie
    search_fields = ["id_subproceso", "nombre_subproceso", "proceso_padre"]
    # There will be a filter on release year
    list_filter = ["id_subproceso", "nombre_subproceso", "proceso_padre"]

# Añadir aqui modelo para indicadores (KPI)

@admin.register(Kpi)
class KpiAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("id_kpi", "nombre_kpi", "descripcion_indicador")
    search_fields = ["id_kpi", "nombre_kpi", "descripcion_indicador"]
    list_filter = ["id_kpi", "nombre_kpi", "descripcion_indicador"]