# Generated by Django 2.2.4 on 2020-03-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AddField(
            model_name='company',
            name='badge',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Логотип'),
        ),
    ]
