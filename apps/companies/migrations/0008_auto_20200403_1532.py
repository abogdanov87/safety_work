# Generated by Django 2.2.6 on 2020-04-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20200403_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
    ]