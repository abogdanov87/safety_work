# Generated by Django 2.2.6 on 2020-04-16 09:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0016_auto_20200415_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.PositiveIntegerField(choices=[(1, 'Медицинское обследование'), (2, 'Инструктаж'), (3, 'Обучение')], default=1, verbose_name='Тип мероприятия')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
                ('event_date', models.DateField(default=datetime.date.today, verbose_name='Дата мероприятия')),
                ('frequency', models.CharField(choices=[('1/m', 'Раз в месяц'), ('1/q', 'Раз в квартал'), ('2/y', 'Два раза в год'), ('1/y', 'Раз в год'), ('1/2y', 'Раз в два года'), ('1/w', 'Раз в неделю')], default='1/m', max_length=20, verbose_name='Тип мероприятия')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='Дата мероприятия')),
                ('certificate', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сертификат')),
                ('employee', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.PROTECT, to='companies.Employee', verbose_name='Сотрудник')),
                ('event', models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.PROTECT, to='companies.Event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Мероприятие - Сотрудник',
                'verbose_name_plural': 'Мероприятия - Сотрудники',
                'db_table': 'event_employee',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='employee',
            field=models.ManyToManyField(through='companies.EventEmployee', to='companies.Employee', verbose_name='Сотрудник'),
        ),
    ]