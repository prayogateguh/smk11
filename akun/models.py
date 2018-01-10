from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from kbm.models import Kelas, Mapel


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    status = models.TextField(max_length=10, default='Siswa')

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
	slug = models.SlugField()
	
	class Meta:
	    verbose_name_plural = 'Siswa'
	
	def __str__(self):
	    return self.user.username
	
	def get_absolute_url(self):
	    return reverse('akun:siswa_detail', args=[self.slug])
	
	def nama_lengkap(self):
	    return "{} {}".format(self.user.first_name, self.user.last_name)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.user)
	    super(Siswa, self).save(*args, **kwargs)
