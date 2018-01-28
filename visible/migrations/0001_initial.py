# Generated by Django 2.0.1 on 2018-01-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='ads')),
                ('link_to_details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventSummaryCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('words', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ImmigrationGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about_them', models.CharField(max_length=120)),
                ('link_to_site', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='partners')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('too_long_to_read', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Image(optional)')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=40)),
                ('venue', models.CharField(max_length=30)),
                ('theme', models.CharField(max_length=60)),
                ('link_to_details', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='previous_events')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('short_summary', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('cost', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='team')),
                ('twitter_link', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(max_length=100)),
                ('linkedIn_link', models.CharField(max_length=100)),
            ],
        ),
    ]
