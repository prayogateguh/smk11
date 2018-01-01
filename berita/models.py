from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class DraftedManager(models.Manager):
    def get_queryset(self):
        return super(DraftedManager, self).get_queryset().filter(status='draft')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True)
    author = models.ForeignKey(User, related_name='news_posts')
    post_pic = models.ImageField(upload_to = 'img/', null=True, blank=True)
    embed = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # the default manager
    published = PublishedManager() # the custom manager
    drafted = DraftedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        permissions = (("can_post_news", "Can post a news"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('berita:post_detail', args=[self.slug,])

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + "-" + slugify(self.title) 
            self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Komentar oleh {} pada {}'.format(self.name, self.post)
