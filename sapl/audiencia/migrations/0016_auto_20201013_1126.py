# Generated by Django 2.2.13 on 2020-10-13 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audiencia', '0015_auto_20200518_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anexoaudienciapublica',
            options={'ordering': ('id',), 'verbose_name': 'Anexo de Documento Acessório', 'verbose_name_plural': 'Anexo de Documentos Acessórios'},
        ),
    ]