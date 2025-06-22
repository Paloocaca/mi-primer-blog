# blog/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto  = models.TextField()

    imagen_url = models.URLField(        # ← aquí irá la URL completa
        blank=True, null=True,
        help_text="Pega el enlace directo (https://…jpg, .png, etc.)"
    )

    fecha_creacion    = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
