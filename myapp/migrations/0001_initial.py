# Generated by Django 4.1 on 2022-08-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('rubrique', models.CharField(max_length=255)),
                ('_2010', models.IntegerField()),
                ('_2011', models.IntegerField()),
                ('_2012', models.IntegerField()),
                ('_2013', models.IntegerField()),
                ('_2014', models.IntegerField()),
                ('_2015', models.IntegerField()),
                ('_2016', models.IntegerField()),
                ('_2017', models.IntegerField()),
                ('_2018', models.IntegerField()),
                ('_2019', models.IntegerField()),
                ('_2020', models.IntegerField()),
                ('_2021', models.IntegerField()),
                ('_2022', models.IntegerField()),
                ('_2023', models.IntegerField()),
                ('_2024', models.IntegerField()),
                ('_2025', models.IntegerField()),
            ],
            options={
                'db_table': 'education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('rubrique', models.CharField(max_length=255)),
                ('janvier', models.IntegerField()),
                ('fevrier', models.IntegerField()),
                ('mars', models.IntegerField()),
                ('avril', models.IntegerField()),
                ('mai', models.IntegerField()),
                ('juin', models.IntegerField()),
                ('juillet', models.IntegerField()),
                ('aout', models.IntegerField()),
                ('septembre', models.IntegerField()),
                ('octobre', models.IntegerField()),
                ('novembre', models.IntegerField()),
                ('decembre', models.IntegerField()),
            ],
            options={
                'db_table': 'BD_DATABASE_PRESIDENCE"."transport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trytable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'trytable',
                'managed': False,
            },
        ),
    ]
