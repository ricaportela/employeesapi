# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=50, verbose_name=b'Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name=b'Nome')),
                ('email', models.TextField(max_length=100, verbose_name=b'E-mail')),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeesapp.Departament', verbose_name=b'Departamento')),
            ],
        ),
    ]
