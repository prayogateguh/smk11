# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-30 04:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kbm', '0008_kelas_mapel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('akun', '0002_auto_20171230_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kelas_siswa', to='kbm.Kelas')),
                ('mapel', models.ManyToManyField(related_name='mapel_siswa', to='kbm.Mapel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Siswa',
            },
        ),
    ]