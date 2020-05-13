# Generated by Django 2.2.6 on 2020-05-13 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20200513_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_type_choice',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.EventType', verbose_name='Вид мероприятия'),
        ),
    ]