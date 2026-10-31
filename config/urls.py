from django.contrib import admin
from django.urls import path

from tienda.views import bienvenida

urlpatterns = [
    path("", bienvenida, name="inicio"),
    path("admin/", admin.site.urls),
]