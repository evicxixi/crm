# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(verbose_name='班级(期)')),
                ('price', models.IntegerField(verbose_name='学费')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('memo', models.CharField(blank=True, max_length=256, null=True, verbose_name='说明')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='课程名称')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='部门名称')),
                ('intro', models.CharField(max_length=64, null=True, verbose_name='部门简介')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='校区名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, null=True, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=64, null=True, verbose_name='密码')),
                ('email', models.CharField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('name', models.CharField(max_length=16, verbose_name='真实姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department', verbose_name='部门')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course', verbose_name='课程名称'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.School', verbose_name='校区'),
        ),
    ]
