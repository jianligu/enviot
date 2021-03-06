# Generated by Django 2.1.4 on 2018-12-10 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('value', models.FloatField()),
                ('units', models.TextField(max_length=20)),
                ('created', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
                'db_table': 'parameter',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.TextField(max_length=30)),
            ],
            options={
                'verbose_name': 'Sensor',
                'verbose_name_plural': 'Sensors',
                'db_table': 'sensor',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
                'db_table': 'site',
            },
        ),
        migrations.CreateModel(
            name='WebMapService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.TextField(max_length=30)),
                ('parameter', models.TextField(max_length=30)),
                ('timestamp', models.TextField(max_length=30)),
                ('endpoint', models.TextField(max_length=200)),
                ('workspace', models.TextField(max_length=20)),
                ('store_name', models.TextField(max_length=50)),
                ('layer_name', models.TextField(max_length=30)),
                ('file_path', models.TextField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sensors', to='monitor.Site'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='parameters', to='monitor.Sensor'),
        ),
    ]
