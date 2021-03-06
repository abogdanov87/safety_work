# Generated by Django 2.2.6 on 2020-05-07 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('companies', '0001_initial'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdocumenttemplate',
            name='document_template',
            field=models.ForeignKey(db_column='document_template_id', on_delete=django.db.models.deletion.PROTECT, to='documents.DocumentTemplate', verbose_name='Документ'),
        ),
        migrations.AddField(
            model_name='eventdocumenttemplate',
            name='event',
            field=models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.PROTECT, to='companies.Event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='event',
            name='commission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Commission', verbose_name='Комиссия'),
        ),
        migrations.AddField(
            model_name='event',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='event',
            name='document_template',
            field=models.ManyToManyField(through='companies.EventDocumentTemplate', to='documents.DocumentTemplate', verbose_name='Документ'),
        ),
        migrations.AddField(
            model_name='event',
            name='employee',
            field=models.ManyToManyField(through='companies.EventEmployee', to='companies.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='event',
            name='previous',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Event', verbose_name='Предыдущее'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.EquipmentGroup', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workplace',
            field=models.ManyToManyField(related_name='employees', to='companies.Workplace', verbose_name='Рабочее место'),
        ),
        migrations.AddField(
            model_name='departmenttype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='department',
            name='department_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.DepartmentType', verbose_name='Тип подразделения'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Department', verbose_name='Вышестоящее подразделение'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ManyToManyField(related_name='user_companies', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='commissionemployee',
            name='commission',
            field=models.ForeignKey(db_column='commission_id', on_delete=django.db.models.deletion.PROTECT, to='companies.Commission', verbose_name='Комиссия'),
        ),
        migrations.AddField(
            model_name='commissionemployee',
            name='employee',
            field=models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.PROTECT, to='companies.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='commission',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='commission',
            name='document_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='documents.DocumentTemplate', verbose_name='Шаблон'),
        ),
        migrations.AddField(
            model_name='commission',
            name='employee',
            field=models.ManyToManyField(through='companies.CommissionEmployee', to='companies.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='education_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.EducationType', verbose_name='Вид обучения'),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='assessmentcard',
            name='harmful_factor',
            field=models.ManyToManyField(to='companies.HarmfulFactor', verbose_name='Вредный фактор'),
        ),
        migrations.AddField(
            model_name='assessmentcard',
            name='work_type',
            field=models.ManyToManyField(to='companies.WorkType', verbose_name='Вид работ'),
        ),
        migrations.AddField(
            model_name='assessmentcard',
            name='working_condition_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.WorkingConditionClass', verbose_name='Класс условий труда'),
        ),
        migrations.AddField(
            model_name='assessmentcard',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Workplace', verbose_name='Рабочее место'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
