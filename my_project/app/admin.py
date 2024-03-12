from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit, UserProfile, Recenzie, Producator

admin.site.register(Produs)
admin.site.register(Favorit)
admin.site.register(UserProfile)
admin.site.register(Recenzie)
admin.site.register(Producator)



