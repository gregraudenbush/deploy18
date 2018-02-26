# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0018_poke_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='poke',
            field=models.CharField(default='poke', max_length=38),
        ),
        migrations.AlterField(
            model_name='poke',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='third_app.User'),
        ),
        migrations.AlterField(
            model_name='poke',
            name='userpoked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='third_app.User'),
        ),
    ]