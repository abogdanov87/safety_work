# Generated by Django 2.2.6 on 2020-05-12 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20200511_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('short_name', models.CharField(default='', max_length=255, verbose_name='Краткое название')),
                ('inn', models.CharField(default='', max_length=20, verbose_name='ИНН')),
                ('badge', models.TextField(blank=True, max_length=100, null=True, verbose_name='Логотип')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Компания',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]