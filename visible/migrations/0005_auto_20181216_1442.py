# Generated by Django 2.0.1 on 2018-12-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visible', '0004_auto_20180128_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previousedition',
            name='theme',
            field=models.CharField(max_length=100),
        ),
    ]
