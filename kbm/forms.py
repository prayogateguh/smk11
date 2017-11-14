from django.contrib.auth.models import User
from .models import Siswa
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ('bio', 'location', 'birth_date')