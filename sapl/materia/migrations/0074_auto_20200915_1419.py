# Generated by Django 2.2.13 on 2020-09-15 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0073_auto_20200910_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numeracao',
            options={'ordering': ('materia', 'tipo_materia', 'numero_materia', 'ano_materia', 'data_materia'), 'verbose_name': 'Numeração de Processo', 'verbose_name_plural': 'Numerações de Processo'},
        ),
    ]
