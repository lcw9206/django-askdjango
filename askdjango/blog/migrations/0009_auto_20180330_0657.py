# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-03-30 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]