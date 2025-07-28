from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil, Gusto

class UserForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': '',
        }

class PerfilForm(forms.ModelForm):
    gustos = forms.ModelMultipleChoiceField(
        queryset=Gusto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Gustos"
    )

    class Meta:
        model = Perfil
        fields = ['carrera', 'semestre', 'foto_perfil', 'gustos']
