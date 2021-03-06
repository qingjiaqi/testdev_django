# Generated by Django 2.0.13 on 2020-06-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('programer', models.CharField(help_text='开发人员', max_length=50, verbose_name='开发人员')),
                ('publish_app', models.CharField(help_text='发布应用', max_length=100, verbose_name='发布应用')),
                ('status', models.BooleanField(default=1, help_text='应用状态', verbose_name='应用状态')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('desc', models.TextField(blank=True, default='', help_text='发布应用', max_length=50, null=True, verbose_name='发布应用')),
            ],
        ),
    ]
