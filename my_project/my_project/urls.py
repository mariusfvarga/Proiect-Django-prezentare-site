"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from app import views
from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.salut, name="home"),
    path("produs/lista", views.lista_produse, name ="pagina-produse" ),
    path("produs/detalui/<int:id>/", views.produs, name="pagina-produs"),
    path("produs/adauga/", views.adauga_produs, name="adauga-produs"),
    path("produs/edit/<int:produs_id>/", views.editare_produs, name="edit-produs"),
    path("produs/recenzie/<int:produs_id>/", views.recenzie_produs, name="recenzie-produs"),
    path("contact", views.contact, name = "contact"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("signup", views.signup, name="signup"),
    path("login", views.custom_login, name="login"), 
    path("logout", views.logout_view, name = "logout"), 
    path("api/", include('rest_framework.urls')),
    path("tinymce/", include('tinymce.urls'))
    
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
