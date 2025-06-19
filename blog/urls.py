from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.lista_public, name=' lista_public'),
    path('evaluacion2/', views.lista_ciclon, name='lista_ciclon') 
] 