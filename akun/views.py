from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm, UserForm
from .models import Guru, Siswa


@login_required
@transaction.atomic
def update_profile(request):

    sts = request.user.profile.status

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('akun:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'akun/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'sts': sts,
            })


@login_required
def guru_detail(request):
    guru = get_object_or_404(Guru, pk=request.user.guru.id,)

    return render(
        request,
        'akun/guru.html',
        {'guru': guru, }
    )


@login_required
def siswa_profile(request):
    siswa = get_object_or_404(Siswa, pk=request.user.siswa.id,)
    return render(
            request,
            'akun/siswa_profile.html',
            {
                'siswa': siswa,
            }
        )


@login_required
def siswa_nilai(request):
    siswa = get_object_or_404(Siswa, pk=request.user.siswa.id,)
    mapel = siswa.mapel.all()

    s1 = []
    s2 = []
    for mpl in mapel:
        s1.append(mpl.mapel_nilai.filter(semester="1"))
        s2.append(mpl.mapel_nilai.filter(semester="2"))

    # n.mapel.kelas
    _1 = [[o for o in n if str(o.mapel.kelas).startswith("X ")] for n in s1]
    a1 = [x for x in _1 if x]
    _2 = [[o for o in n if str(o.mapel.kelas).startswith("X ")] for n in s2]
    a2 = [x for x in _2 if x]
    x = [a1, a2]  # nilai kelas X
    _1 = [[o for o in n if str(o.mapel.kelas).startswith("XI ")] for n in s1]
    b1 = [x for x in _1 if x]
    _2 = [[o for o in n if str(o.mapel.kelas).startswith("XI ")] for n in s2]
    b2 = [x for x in _2 if x]
    xi = [b1, b2]  # nilai kelas XI
    _1 = [[o for o in n if str(o.mapel.kelas).startswith("XII ")] for n in s1]
    c1 = [x for x in _1 if x]
    _2 = [[o for o in n if str(o.mapel.kelas).startswith("XII ")] for n in s2]
    c2 = [x for x in _2 if x]
    xii = [c1, c2]  # nilai kelas XII
    nilai = [x, xi, xii]

    return render(
        request,
        'akun/siswa_nilai.html',
        {
            'siswa': siswa,
            'mapel': mapel,
            'nilai': nilai,
        }
    )
