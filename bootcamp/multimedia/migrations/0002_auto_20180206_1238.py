# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 12:38
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multimedia_link', models.FileField(upload_to='media/')),
                ('title', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('categorie', models.CharField(choices=[('F', 'File'), ('V', 'Video'), ('A', 'Audio')], default='V', max_length=1)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Multimedia',
                'verbose_name_plural': 'Multimedias',
            },
        ),
        migrations.RemoveField(
            model_name='videolink',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='videolink',
            name='update_user',
        ),
        migrations.DeleteModel(
            name='VideoLink',
        ),
    ]
