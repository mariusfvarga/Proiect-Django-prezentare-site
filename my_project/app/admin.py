from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit, UserProfile

admin.site.register(Produs)
admin.site.register(Favorit)
admin.site.register(UserProfile)


