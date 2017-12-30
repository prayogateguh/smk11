from django.core.urlresolvers import reverse
from django.db import models
# from django.template.defaultfilters import slugify


# class Kelas(models.Model):
#     name = models.CharField(max_length=10)
#     slug = models.SlugField()

#     class Meta:
#         verbose_name = 'Kelas'
#         verbose_name_plural = 'Kelas'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('kbm:kelas_detail', args=[self.slug,])

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Kelas, self).save(*args, **kwargs)

# class Mapel(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     kelas = models.ManyToManyField(Kelas, related_name='mapel_kelas')
#     slug = models.SlugField(unique=True)
#     hari = models.CharField(max_length=50,)

#     class Meta:
#         verbose_name = 'Mapel'
#         verbose_name_plural = 'Mapel'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('kbm:mapel_detail', args=[self.slug])

#     # def get_hari(self):
#     #     return ", ".join([ha.name for ha in self.hari.all()])

#     def get_kelas(self):
#         return ", ".join([kl.name for kl in self.kelas.all()])

# class NilaiMapel(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     angka = models.IntegerField()
#     mapel = models.OneToOneField(Mapel, related_name='mapel_nilai')
#     siswa = models.ForeignKey(Siswa, related_name='siswa_nilai')

#     class Meta:
#         verbose_name = 'Nilai'
#         verbose_name_plural = 'Nilai'

#     def kelas(self):
#         return self.siswa.kelas
