# Generated by Django 2.2.6 on 2020-04-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0017_auto_20200416_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventemployee',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Статус активности'),
        ),
    ]