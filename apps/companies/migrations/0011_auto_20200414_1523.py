# Generated by Django 2.2.6 on 2020-04-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_auto_20200414_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commissionemployee',
            options={'verbose_name': 'Комиссия - Сотрудник', 'verbose_name_plural': 'Комиссии - Сотрудники'},
        ),
    ]