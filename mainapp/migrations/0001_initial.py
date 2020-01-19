# Generated by Django 2.2.6 on 2019-11-05 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=700)),
                ('wikiinfo', models.TextField(default='wikiinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=700)),
                ('wikiinfo', models.TextField(default='wikiinfo')),
                ('wikiinfolink', models.CharField(default='wikiinfolink', max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordid', models.CharField(default='recordid', max_length=100)),
                ('title', models.CharField(default='title', max_length=700)),
                ('barcode', models.CharField(default='barcode', max_length=100)),
                ('unit', models.CharField(default='unit', max_length=100)),
                ('recordformat', models.CharField(default='recordformat', max_length=100)),
                ('price', models.CharField(default='price', max_length=100)),
                ('precision', models.CharField(default='precision', max_length=100)),
                ('delivery', models.CharField(default='delivery', max_length=100)),
                ('stock', models.CharField(default='stock', max_length=100)),
                ('date', models.CharField(default='date', max_length=100)),
                ('wikiinfo', models.TextField(default='wikiinfo')),
                ('wikilink', models.CharField(default='wikilink', max_length=500)),
                ('discogspicurl', models.CharField(default='discogpicurl', max_length=500)),
                ('ytlink', models.CharField(default='ytlink', max_length=500)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Artist')),
                ('label', models.ForeignKey(default='label', on_delete=django.db.models.deletion.PROTECT, to='mainapp.Label')),
            ],
        ),
    ]