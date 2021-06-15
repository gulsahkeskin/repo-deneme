# Generated by Django 3.1.7 on 2021-06-09 15:36

from django.conf import settings
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_keywords', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('search', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('wikidata_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_id', models.CharField(max_length=16)),
                ('journal_title', models.CharField(max_length=255)),
                ('article_title', models.TextField(max_length=511)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField(null=True)),
                ('tags', models.CharField(default='', max_length=255)),
                ('authors', models.ManyToManyField(to='Tagapp.Author')),
                ('related_keywords', models.ManyToManyField(to='Tagapp.RelatedKeywords')),
            ],
        ),
    ]
