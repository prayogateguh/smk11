from django.contrib import admin
from .models import Kelas, Mapel, NilaiMapel


@admin.register(Mapel)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_kelas', 'hari',)
    fields = ('name', 'kelas', 'hari',)


@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    fields = ('name',)
    ordering = ('-name',)

    # prepopulated_fields = {'slug': ('id',), }


@admin.register(NilaiMapel)
class NilaiMapelAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'kelas', 'mapel', 'pengetahuan', 'keterampilan', )
