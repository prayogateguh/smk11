from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm, SiswaForm, UserForm
from .models import Siswa, Guru


@login_required
def dashboard(request):
    return render(request, 'akun/dashboard.html', {})


@login_required
@transaction.atomic
def update_profile(request):

    sts = request.user.profile.status

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if sts == 'Siswa':
            status_form = SiswaForm(request.POST, instance=request.user)
        elif sts == 'Guru':
            pass
        elif sts == 'Staff':
            pass
        else:
            pass
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
        status_form = SiswaForm(instance=request.user)

    return render(request, 'akun/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'status_form': status_form,
            'sts': sts,
            })


@login_required
def siswa_detail(request):
    siswa = get_object_or_404(Siswa, pk=request.user.siswa.id,)

    return render(
        request,
        'akun/siswa.html',
        {'siswa': siswa, }
    )


@login_required
def guru_detail(request):
    guru = get_object_or_404(Guru, pk=request.user.guru.id,)

    return render(
        request,
        'akun/guru.html',
        {'guru': guru, }
    )
