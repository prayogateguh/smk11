from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Kelas(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Kelas'
        verbose_name_plural = 'Kelas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbm:kelas_detail', args=[self.slug, ])

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Kelas.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Mapel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kelas = models.ManyToManyField(Kelas, related_name='mapel_kelas')
    slug = models.SlugField(unique=True)
    hari = models.CharField(max_length=50,)
    tahun_ajaran = models.CharField(max_length=4,)

    class Meta:
        verbose_name = 'Mapel'
        verbose_name_plural = 'Mapel'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbm:mapel_detail', args=[self.slug])

    def get_kelas(self):
        return ", ".join([kl.name for kl in self.kelas.all()])

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Mapel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class NilaiMapel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pengetahuan = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0.0,
        null=True)
    keterampilan = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0.0,
        null=True)

    smt = [('smt1', 'SEMESTER 1'), ('smt2', 'SEMESTER 2')]
    semester = models.CharField(
        max_length=10, choices=smt, default='SEMESTER 1')
    mapel = models.ForeignKey(Mapel, related_name='mapel_nilai')
    siswa = models.ForeignKey(
        User, related_name='siswa_nilai')

    def get_siswa(self):
        if self.siswa.first_name and self.siswa.last_name:
            nama = self.siswa.first_name + ' ' + self.siswa.last_name
        else:
            nama = self.siswa.username
        return nama

    class Meta:
        verbose_name = 'Nilai'
        verbose_name_plural = 'Nilai'

    def kelas(self):
        return self.siswa.siswa.kelas

    def __str__(self):
        return self.mapel.name
