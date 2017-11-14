from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        return reverse('kbm:kelas_detail', args=[self.slug,])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Kelas, self).save(*args, **kwargs)

class Mapel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kelas = models.ManyToManyField(Kelas, related_name='mapel_kelas')
    slug = models.SlugField(unique=True)
    hari = models.CharField(max_length=50,)

    class Meta:
        verbose_name = 'Mapel'
        verbose_name_plural = 'Mapel'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbm:mapel_detail', args=[self.slug])

    # def get_hari(self):
    #     return ", ".join([ha.name for ha in self.hari.all()])

    def get_kelas(self):
        return ", ".join([kl.name for kl in self.kelas.all()])

class NilaiMapel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    angka = models.IntegerField()
    mapel = models.OneToOneField(Mapel, related_name='mapel_nilai')
    siswa = models.ForeignKey('Siswa', related_name='siswa_nilai')

    class Meta:
        verbose_name = 'Nilai'
        verbose_name_plural = 'Nilai'

    def kelas(self):
        return self.siswa.kelas

class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, related_name='kelas_siswa')
    mapel = models.ManyToManyField('Mapel', related_name='mapel_siswa')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Siswa'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('kbm:siswa_detail', args=[self.slug])

    def nama_lengkap(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Siswa.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.siswa.save()
