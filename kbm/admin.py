from django.contrib import admin
from .models import Kelas, Mapel, NilaiMapel


@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('name', 'tahun_ajaran', 'slug',)
    fields = ('name', 'tahun_ajaran',)
    ordering = ('tahun_ajaran', '-name',)


class NilaiInline(admin.TabularInline):
    fields = ('siswa', 'semester', 'pengetahuan', 'keterampilan',)
    model = NilaiMapel
    extra = 0


@admin.register(Mapel)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('name', 'kelas', 'hari', 'slug',)
    fields = ('name', 'kelas', 'hari',)

    inlines = [NilaiInline, ]
