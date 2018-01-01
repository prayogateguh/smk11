from django.contrib.auth.models import User

from django import forms

from akun.models import Siswa

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ('user', 'kelas', 'mapel', 'slug')