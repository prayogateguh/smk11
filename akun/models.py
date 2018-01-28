from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from kbm.models import Kelas, Mapel


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biodata = models.TextField(max_length=500, blank=True, null=True)
    alamat = models.CharField(max_length=150, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, default='Siswa')
    no_hp = models.CharField(max_length=15, default='-')
    nama_ayah = models.CharField(max_length=50, default='-')
    nama_ibu = models.CharField(max_length=50, default='-')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# automatically create the user profile
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, related_name='kelas_siswa')
    mapel = models.ManyToManyField(Mapel, related_name='mapel_siswa')
    semester = models.IntegerField(default=1)
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = 'Siswa'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('akun:siswa_detail', args=[self.slug])

    def nama_lengkap(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def _get_unique_slug(self):
        slug = slugify(self.user)
        unique_slug = slug
        num = 1
        while Siswa.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Guru(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ngajar_kelas = models.ManyToManyField(Kelas, related_name='ngajar_kelas')
    ngajar_mapel = models.ManyToManyField(Mapel, related_name='ngajar_mapel')
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = 'Guru'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('akun:guru_detail', args=[self.slug])

    def nama_lengkap(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def _get_unique_slug(self):
        slug = slugify(self.user)
        unique_slug = slug
        num = 1
        while Guru.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
