from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.lista_public, name=' lista_public'),
    path('evaluacion2/', views.lista_ciclon, name='lista_ciclon') 
<<<<<<< HEAD
] 
=======
] 
>>>>>>> 084297658d78520c7cb22be9fb2e37cf1321f339
