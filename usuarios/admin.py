from django.contrib import admin
from .models import CategoriaGusto, SubcategoriaGusto, Gusto, Perfil

admin.site.register(CategoriaGusto)
admin.site.register(SubcategoriaGusto)
admin.site.register(Gusto)
admin.site.register(Perfil)
