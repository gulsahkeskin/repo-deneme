# Generated by Django 3.1.7 on 2021-06-10 18:01

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tagapp', '0008_auto_20210609_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]