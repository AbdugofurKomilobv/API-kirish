# Generated by Django 5.2 on 2025-04-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('birth_day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('year', models.IntegerField(default=1900)),
                ('genre', models.TextField()),
                ('actors', models.ManyToManyField(related_name='actors', to='configapp.actors')),
            ],
        ),
    ]
