from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Kelas, Mapel


@login_required
def semua_kelas(request):
    kelas = Kelas.objects.all()

    return render(request, 'kbm/kelas.html', {'kelas': kelas, })


@login_required
def semua_mapel(request):
    mapel = Mapel.objects.all()

    return render(request, 'kbm/mapel.html', {'mapel': mapel, })


@login_required
def kelas_detail(request, slug):
    kelas = get_object_or_404(Kelas, slug=slug,)
    guru = kelas.ngajar_kelas.get(user=request.user)
    mapel = guru.ngajar_mapel.filter(kelas=kelas,)

    return render(
        request,
        'kbm/kelas_detail.html',
        {
            'kelas': kelas,
            'guru': guru,
            'mapel': mapel,
        }
    )


@login_required
def mapel_detail(request, slug):
    mapel = get_object_or_404(Mapel, slug=slug,)
    guru = mapel.ngajar_mapel.get(user=request.user)
    _nil_smt_1 = mapel.mapel_nilai.filter(semester="1")
    _nil_smt_2 = mapel.mapel_nilai.filter(semester="2")
    nilai_semester = [_nil_smt_1, _nil_smt_2]

    return render(
        request,
        'kbm/mapel_detail.html',
        {
            'mapel': mapel,
            'guru': guru,
            'nilai_semester': nilai_semester,
        },
    )
