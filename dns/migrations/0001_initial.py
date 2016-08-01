# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
                'db_table': 'a',
            },
        ),
        migrations.CreateModel(
            name='CNAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cname',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(choices=[('DEFAULT', '\u9ed8\u8ba4'), ('CNC', '\u7f51\u901a'), ('CT', '\u7535\u4fe1'), ('CMCC', '\u79fb\u52a8'), ('EDU', '\u6559\u80b2\u7f51')], default='DEFAULT', max_length=20)),
            ],
            options={
                'db_table': 'line',
            },
        ),
        migrations.CreateModel(
            name='TXT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='txt', to='dns.Domain')),
            ],
            options={
                'db_table': 'txt',
            },
        ),
        migrations.AddField(
            model_name='domain',
            name='line',
            field=models.ManyToManyField(to='dns.Line'),
        ),
        migrations.AddField(
            model_name='cname',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cname', to='dns.Domain'),
        ),
        migrations.AddField(
            model_name='a',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='dns.Domain'),
        ),
    ]