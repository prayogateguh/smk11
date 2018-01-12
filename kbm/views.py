from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Kelas, Mapel


@login_required
def semua_kelas(request):
    kelas = Kelas.objects.all()

    return render(request, 'kbm/kelas.html', {'kelas': kelas, })


@login_required
def kelas_detail(request, slug):
    kelas = get_object_or_404(Kelas, slug=slug,)
    guru = kelas.ngajar_kelas.get(user=request.user)

    return render(
        request,
        'kbm/kelas_detail.html',
        {'kelas': kelas, 'guru': guru, }
    )


@login_required
def semua_mapel(request):
    mapel = Mapel.objects.all()

    return render(request, 'kbm/mapel.html', {'mapel': mapel, })


@login_required
def mapel_detail(request, slug):
    mapel = get_object_or_404(Mapel, slug=slug,)

    return render(request, 'kbm/mapel_detail.html', {'mapel': mapel, })
