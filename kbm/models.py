from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Kelas(models.Model):
    name = models.CharField(max_length=25)
    tahun_ajaran = models.CharField(max_length=9, default="2017/2018")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Kelas'
        verbose_name_plural = 'Kelas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbm:kelas_detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        super(Kelas, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id)
            self.save()
        if self.tahun_ajaran not in self.name:
            # add tahun ke nama
            self.name += " - " + self.tahun_ajaran
            self.save()


class Mapel(models.Model):
    name = models.CharField(max_length=100)
    kelas = models.ForeignKey(Kelas, related_name='mapel_kelas')
    hari = models.CharField(max_length=50,)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Mapel'
        verbose_name_plural = 'Mapel'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbm:mapel_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # save it to get the id
        super(Mapel, self).save(*args, **kwargs)
        # setting the slug and add by id
        if not self.slug:
            self.slug = str(self.id)
            self.save()
        if str(self.kelas) not in self.name:
            self.name += " - " + str(self.kelas)
            self.save()


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

    smt = [
        ('1', 'SEMESTER 1'),
        ('2', 'SEMESTER 2'),
    ]
    semester = models.CharField(
        max_length=10, choices=smt, default='SEMESTER 1')
    mapel = models.ForeignKey(Mapel, related_name='mapel_nilai')
    siswa = models.ForeignKey(
        User, related_name='siswa_nilai')

    class Meta:
        verbose_name = 'Nilai'
        verbose_name_plural = 'Nilai'

    def __str__(self):
        return self.mapel.name
