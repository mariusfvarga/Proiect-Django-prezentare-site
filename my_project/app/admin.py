from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

# Register your models here.
from .models import Produs, Favorit, UserProfile, Recenzie, Producator


admin.site.register(Favorit)
admin.site.register(UserProfile)
admin.site.register(Recenzie)
admin.site.register(Producator)

def retrage_din_oferta(modeladmin, request, queryset):
    queryset.update(stoc=0)
    
class ProdusAdmin(admin.ModelAdmin):
    search_fields = ("titlu", "producator__nume")
    list_display = ("titlu", "producator", "stoc", "pret")
    list_filter = ("producator", )
    list_per_page = 20
    list_select_related = ("producator", )
    list_editable = ("stoc", )
    actions = (retrage_din_oferta, )
    
    
    

admin.site.register(Produs, ProdusAdmin)


