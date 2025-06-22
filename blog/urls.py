from django.urls import path
from . import views

urlpatterns = [
    path("evaluacion2", views.lista_public, name="lista_public"),
    path("nota/<int:pk>/", views.detalle_publicacion, name="detalle_publicacion"),
]
