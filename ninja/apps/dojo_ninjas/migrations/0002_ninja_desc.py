# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='desc',
            field=models.TextField(default='This wass added'),
            preserve_default=False,
        ),
    ]