# Generated by Django 2.2.6 on 2020-05-13 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20200512_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='event_type_choice',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='commission_type',
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Наименование')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Вид мероприятия',
                'verbose_name_plural': 'Виды мероприятий',
                'db_table': 'event_type',
            },
        ),
    ]
