# Generated by Django 3.0 on 2019-12-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20191214_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
