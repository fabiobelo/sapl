# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0046_auto_20190417_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomaterialegislativa',
            name='sequencia_numeracao',
            field=models.CharField(blank=True, choices=[('A', 'Sequencial por ano'), ('L', 'Sequencial por legislatura'), ('U', 'Sequencial único')], max_length=1, verbose_name='Sequência de numeração'),
        ),
    ]
