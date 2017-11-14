from django.contrib import admin
from .models import Kelas, Siswa, Mapel, NilaiMapel

@admin.register(Mapel)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_kelas', 'hari',)

@admin.register(NilaiMapel)
class NilaiMapelAdmin(admin.ModelAdmin):
    list_display = ('angka', 'siswa', 'mapel', 'kelas',)

@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    fields = ('name',)
    ordering = ('-name',)
    
    #prepopulated_fields = {'slug': ('id',), }

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'kelas', 'user')