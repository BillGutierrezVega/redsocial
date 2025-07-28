from django.db import models
from django.contrib.auth.models import User

class CategoriaGusto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class SubcategoriaGusto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaGusto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"

class Gusto(models.Model):
    nombre = models.CharField(max_length=100)
    subcategoria = models.ForeignKey(SubcategoriaGusto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.subcategoria.nombre})"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)
    semestre = models.PositiveSmallIntegerField()
    gustos = models.ManyToManyField(Gusto, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='fotos_perfil/default.png')

    def __str__(self):
        return f"{self.user.username} - {self.carrera} ({self.semestre}° semestre)"
