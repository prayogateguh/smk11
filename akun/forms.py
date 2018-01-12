from django import forms
from django.contrib.auth.models import User

from .models import Profile, Siswa


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('biodata', 'tanggal_lahir', 'alamat',)


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ('kelas', 'mapel',)
