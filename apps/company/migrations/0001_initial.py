# Generated by Django 2.2.4 on 2019-10-13 12:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('short_name', models.CharField(default='', max_length=255, verbose_name='Краткое название')),
                ('inn', models.CharField(default='', max_length=20, verbose_name='ИНН')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Код подразделения')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Название')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Компания')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='company.Department', verbose_name='Вышестоящее подразделение')),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='DepartmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
            ],
            options={
                'db_table': 'department_type',
            },
        ),
        migrations.CreateModel(
            name='EducationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
                ('frequency', models.CharField(default='', max_length=50, verbose_name='Периодичность')),
            ],
            options={
                'db_table': 'education_type',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Код инструмента')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Название')),
                ('inventory_number', models.CharField(default='', max_length=255, verbose_name='Инвентарный номер')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Компания')),
            ],
            options={
                'db_table': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='EquipmentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Название')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
            ],
            options={
                'db_table': 'equipment_group',
            },
        ),
        migrations.CreateModel(
            name='HarmfulFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Номер')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
                ('inspection_frequency', models.CharField(default='', max_length=50, verbose_name='Периодичность осмотра')),
            ],
            options={
                'db_table': 'harmful_factor',
            },
        ),
        migrations.CreateModel(
            name='MedicalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
            ],
            options={
                'db_table': 'medical_type',
            },
        ),
        migrations.CreateModel(
            name='MemberStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
            ],
            options={
                'db_table': 'member_status',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Код должности')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Название')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Компания')),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Ppe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
            ],
            options={
                'db_table': 'ppe',
            },
        ),
        migrations.CreateModel(
            name='PsychiatricType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
            ],
            options={
                'db_table': 'psychiatric_type',
            },
        ),
        migrations.CreateModel(
            name='WorkingConditionClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Класс')),
            ],
            options={
                'db_table': 'working_condition_class',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Номер')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
                ('inspection_frequency', models.CharField(default='', max_length=50, verbose_name='Периодичность осмотра')),
            ],
            options={
                'db_table': 'work_type',
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=30, verbose_name='Код рабочего места')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Название')),
                ('instruction_required', models.BooleanField(default=True, verbose_name='Необходимость проходить инструктаж по электробезопасности')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Department', verbose_name='Подразделение')),
                ('equipment', models.ManyToManyField(to='company.Equipment', verbose_name='Инструмент')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Position', verbose_name='Должность')),
            ],
            options={
                'db_table': 'workplace',
            },
        ),
        migrations.CreateModel(
            name='PpeStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decree', models.CharField(default='', max_length=2000, verbose_name='Основание')),
                ('paragraph', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер пункта')),
                ('item_count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('ppe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Ppe', verbose_name='СИЗ')),
            ],
            options={
                'db_table': 'ppe_standard',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='company.EquipmentGroup', verbose_name='Группа'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(default='', max_length=255, verbose_name='Отчество')),
                ('address', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Адрес проживания')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Дата рождения')),
                ('sex', models.CharField(blank=True, choices=[('m', 'мужчина'), ('f', 'женщина')], max_length=1, null=True, verbose_name='Пол')),
                ('disability', models.BooleanField(blank=True, null=True, verbose_name='Инвалидность')),
                ('employment_date', models.DateField(default=datetime.date.today, verbose_name='Дата приема на работу')),
                ('pers_number', models.CharField(default='', max_length=255, verbose_name='Табельный номер')),
                ('insurance_number', models.CharField(default='', max_length=255, verbose_name='Страховой номер (СНИЛС)')),
                ('fire_date', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Компания')),
                ('workplace', models.ManyToManyField(to='company.Workplace', verbose_name='Рабочее место')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.DepartmentType', verbose_name='Тип подразделения'),
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=1, verbose_name='№ п/п')),
                ('name', models.CharField(default='', max_length=2000, verbose_name='Наименование')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Employee', verbose_name='Сотрудник')),
                ('member_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.MemberStatus', verbose_name='Статус участника')),
            ],
            options={
                'db_table': 'commission',
            },
        ),
        migrations.CreateModel(
            name='CertificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_date', models.DateField(default=datetime.date.today, verbose_name='Дата обучения')),
                ('id_number', models.CharField(default='', max_length=50, verbose_name='Номер удостоверения')),
                ('next_education_date', models.DateField(default=datetime.date.today, verbose_name='Контрольная дата очередной аттестации')),
                ('days_to_education', models.PositiveIntegerField(blank=True, null=True, verbose_name='Дней до очередной аттестации')),
                ('education_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.EducationType', verbose_name='Вид обучения')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Employee', verbose_name='Сотрудник')),
            ],
            options={
                'db_table': 'certification_type',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=1, verbose_name='Номер п.п')),
                ('certificate_number', models.CharField(default='', max_length=255, verbose_name='Номер сертификата')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Примечание')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Компания')),
            ],
            options={
                'db_table': 'certificate',
            },
        ),
        migrations.CreateModel(
            name='AssessmentCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(default='', max_length=50, verbose_name='Номер карты')),
                ('signing_date', models.DateField(blank=True, null=True, verbose_name='Дата подписания карты')),
                ('next_assessment_date', models.DateField(blank=True, null=True, verbose_name='Дата следующей оценки')),
                ('medical_inspection', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=1, verbose_name='Проведение медицинских осмотров')),
                ('increased_pay', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Повышенная оплата труда')),
                ('extra_vacation', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Дополнительный отпуск')),
                ('reduced_working_hours', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Сокращенная продолжительность рабочего дня')),
                ('milk', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Молоко')),
                ('therapeutic_nutrition', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Лечебно-профилактическое питание')),
                ('early_retirement', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')], default=0, verbose_name='Право на досрочное назначение страховой пенсии')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('harmful_factor', models.ManyToManyField(to='company.HarmfulFactor', verbose_name='Вредный фактор')),
                ('work_type', models.ManyToManyField(to='company.WorkType', verbose_name='Вид работ')),
                ('working_condition_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.WorkingConditionClass', verbose_name='Класс условий труда')),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Workplace', verbose_name='Рабочее место')),
            ],
            options={
                'db_table': 'assessment_card',
            },
        ),
    ]