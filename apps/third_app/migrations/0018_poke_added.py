# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0017_poke_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='poke',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]