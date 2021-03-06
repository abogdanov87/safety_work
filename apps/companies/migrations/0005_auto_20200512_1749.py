# Generated by Django 2.2.6 on 2020-05-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_historicalcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Код инструмента'),
        ),
        migrations.AlterField(
            model_name='harmfulfactor',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='position',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Код должности'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Код рабочего места'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер'),
        ),
    ]
