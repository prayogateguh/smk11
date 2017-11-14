from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic

from .forms import SiswaForm, UserForm
from .models import Kelas, Mapel, Siswa


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        siswa_form = SiswaForm(request.POST, instance=request.user.siswa)
        if user_form.is_valid() and siswa_form.is_valid():
            user_form.save()
            siswa_form.save()
            return redirect('akun:dashboard')
    else:
        user_form = UserForm(instance=request.user)
        siswa_form = SiswaForm(instance=request.user.siswa)
    return render(request, 'kbm/profile.html', {
        'user_form': user_form,
        'siswa_form': siswa_form
    })

@login_required
def semua_kelas(request):
    kelas = Kelas.objects.all()

    return render(request, 'kbm/kelas.html', {'kelas': kelas,})

@login_required
def kelas_detail(request, slug):
    kelas = get_object_or_404(Kelas, slug=slug,)
    mapel = kelas.mapel_kelas.all()
    siswa = kelas.kelas_siswa.all()

    return render(request, 'kbm/kelas_detail.html', {'kelas':kelas, 'siswa':siswa, 'mapel':mapel,})

@login_required
def semua_mapel(request):
    mapel = Mapel.objects.all()

    return render(request, 'kbm/mapel.html', {'mapel': mapel,})

@login_required
def mapel_detail(request, pk):
    mapel = get_object_or_404(Mapel, slug=pk,)

    return render(request, 'kbm/mapel_detail.html', {'mapel':mapel,})

@login_required
def semua_siswa(request):
    siswa = Siswa.objects.all()

    return render(request, 'kbm/siswa.html', {'siswa': siswa,})

@login_required
def siswa_detail(request, pk):
    siswa = get_object_or_404(Siswa, slug=pk,)
    nilai = siswa.siswa_nilai.all()

    return render(request, 'kbm/siswa_detail.html', {'siswa':siswa, 'nilai':nilai,})