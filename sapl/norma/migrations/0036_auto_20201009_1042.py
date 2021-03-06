# Generated by Django 2.2.13 on 2020-10-09 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0035_auto_20200609_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anexonormajuridica',
            options={'ordering': ('id',), 'verbose_name': 'Anexo da Norma Juridica', 'verbose_name_plural': 'Anexos da Norma Juridica'},
        ),
        migrations.AlterModelOptions(
            name='legislacaocitada',
            options={'ordering': ('id',), 'verbose_name': 'Legislação', 'verbose_name_plural': 'Legislações'},
        ),
        migrations.AlterModelOptions(
            name='normaestatisticas',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='tipovinculonormajuridica',
            options={'ordering': ('id',), 'verbose_name': 'Tipo de Vínculo entre Normas Jurídicas', 'verbose_name_plural': 'Tipos de Vínculos entre Normas Jurídicas'},
        ),
    ]
