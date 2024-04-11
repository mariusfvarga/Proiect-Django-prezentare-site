from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit, UserProfile, Recenzie, Producator


admin.site.register(Favorit)
admin.site.register(UserProfile)
admin.site.register(Recenzie)
admin.site.register(Producator)

class ProdusAdmin(admin.ModelAdmin):
    search_fields = ("titlu", )
    list_display = ("titlu", "producator", "stoc", "pret")
    list_filter = ("producator", )

admin.site.register(Produs, ProdusAdmin)


