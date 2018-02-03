from django.contrib import admin
from .models import Profile, Siswa, Guru


@admin.register(Profile)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'biodata', 'tanggal_lahir', 'alamat')


@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug',)
    fields = ('user', 'ngajar_kelas', 'ngajar_mapel',)


@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('user', 'kelas', 'slug',)
    fields = ('user', 'kelas', 'mapel',)
