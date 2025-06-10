from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def lista_public(request):
	publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
	usr_id=request.GET.get('ususario')
	if usr_id:
		publicaciones=publicaciones.filter(autor_id=usr_id)
	ususarios=User.objects.all()
	if usr_id:
        usuario_activo = int(usr_id)
	else:
		usuario_activo = None
	return render(request, 'blog/lista_public.html',{
		'publicaciones': publicaciones,
		'usuarios':usuarios,
		'usuario_activo':usuario_activo

	})
def lista_ciclon(request):
		return render(request, 'blog/lista_ciclon')
