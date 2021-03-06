# Generated by Django 2.2.6 on 2020-05-18 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_position_company_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventemployee',
            name='event_instance',
            field=models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='companies.Event', verbose_name='Мероприятие'),
        ),
    ]
