# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0023_auto_20160915_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome do Bloco')),
                ('data_criacao', models.DateField(blank=True, null=True, verbose_name='Data Criação')),
                ('data_extincao', models.DateField(blank=True, null=True, verbose_name='Data Dissolução')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('bancadas', models.ManyToManyField(blank=True, to='sessao.Bancada', verbose_name='Bancadas')),
            ],
            options={
                'verbose_name_plural': 'Blocos',
                'verbose_name': 'Bloco',
            },
        ),
    ]
