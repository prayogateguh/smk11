from django.contrib import admin
from .models import Profile, Siswa

@admin.register(Profile)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'bio', 'birth_date', 'location')

@admin.register(Siswa)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('user', 'kelas', 'slug',)
    fields = ('user', 'kelas', 'mapel',)