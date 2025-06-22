# blog/views.py
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from .models import Publicacion


def lista_public(request):
    """
    - Muestra las publicaciones con fecha ≤ ahora.
    - Permite filtrar por ?usuario=<id>.
    - Soporta paginación con ?page=<n>.
    """
    # 1. Query base optimizada
    publicaciones_qs = (
        Publicacion.objects
        .select_related("autor")                     # evita 1 + N al mostrar autor
        .filter(fecha_publicacion__lte=timezone.now())
        .order_by("-fecha_publicacion")              # más reciente primero
    )

    # 2. Filtro por usuario
    usr_id = request.GET.get("usuario")
    usuario_activo = None
    if usr_id:
        try:
            usuario_activo = int(usr_id)
            publicaciones_qs = publicaciones_qs.filter(autor_id=usuario_activo)
        except (ValueError, User.DoesNotExist):
            usuario_activo = None  # id inválido → sin filtrar

    # 3. Paginación (10 por página)
    paginator = Paginator(publicaciones_qs, 10)
    page_number = request.GET.get("page")
    try:
        publicaciones = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        publicaciones = paginator.page(1)

    context = {
        "publicaciones": publicaciones,
        "usuarios": User.objects.only("id", "username").order_by("username"),
        "usuario_activo": usuario_activo,
    }
    return render(request, "blog/lista_public.html", context)


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, "blog/detalle_publicacion.html", {"publicacion": publicacion})