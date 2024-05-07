# Generated by Django 3.2.16 on 2023-07-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('password2', models.CharField(max_length=40)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('surname', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('fathers_name', models.CharField(max_length=40)),
                ('t_number', models.CharField(max_length=11, unique=True)),
                ('workplace', models.TextField()),
                ('position', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('password2', models.CharField(max_length=40)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('klapan', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('fathers_name', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('date_of_operation', models.DateField()),
                ('date_of_death', models.DateField()),
                ('height', models.CharField(max_length=5)),
                ('seria_number_klapan', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=40)),
                ('cardiac_pressure', models.CharField(max_length=40)),
                ('heart_pulse', models.CharField(max_length=40)),
                ('illnesses', models.TextField()),
                ('drugs', models.TextField()),
                ('comments', models.TextField()),
                ('date_of_made_klapan', models.DateField()),
                ('manufacturer', models.CharField(max_length=40)),
            ],
        ),
    ]
