# Generated by Django 2.2.6 on 2020-04-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20200422_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttemplate',
            name='file_template',
            field=models.FileField(blank=True, null=True, upload_to='doc_templates/', verbose_name='Файл шаблона'),
        ),
    ]
