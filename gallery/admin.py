from django.contrib import admin
from gallery.models import Fotografia

# Register your models here.
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada","data_fotografia")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias) 