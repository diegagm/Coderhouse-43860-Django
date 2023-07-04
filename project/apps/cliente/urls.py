from django.urls import path

from .views import crear_clientes, home

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('crear_clientes/', crear_clientes, name="crear_clientes")
]
