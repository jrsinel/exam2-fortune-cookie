# Generated by Django 2.0.6 on 2018-06-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeedFortune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Seed Fortune',
                'verbose_name_plural': 'Seed Fortunes',
                'db_table': 'seed_fortune',
            },
        ),
    ]