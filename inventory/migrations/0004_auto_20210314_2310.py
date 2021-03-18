# Generated by Django 2.2.19 on 2021-03-15 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210305_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='remedy name')),
                ('quantity', models.IntegerField()),
                ('units', models.CharField(max_length=30)),
                ('source_of_herbs', models.TextField()),
                ('date_made', models.DateField()),
                ('best_by_date', models.DateField()),
                ('contains_alcohol', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('tincture', 'Tincture'), ('dried', 'Dried'), ('oil', 'Oil'), ('glycerite', 'Glycerite'), ('tea_blend', 'Tea blend'), ('fire_cider', 'Fire cider'), ('salve', 'Salve'), ('throat_spray', 'Throat spray'), ('wound_spray', 'Wound spray'), ('bitters', 'Bitters'), ('syrup', 'Syrup')], default='tincture', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Donor')),
                ('herbs', models.ManyToManyField(to='inventory.Herb')),
            ],
        ),
        migrations.CreateModel(
            name='RemedyInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='remedy name')),
                ('quantity', models.IntegerField()),
                ('units', models.CharField(choices=[('ounces', 'ounces'), ('1_oz_jar', '1 oz jars'), ('2_oz_jar', '2 oz jars'), ('4_oz_jar', '4 oz jars')], default='ounces', max_length=20)),
                ('type', models.CharField(choices=[('tincture', 'Tincture'), ('dried', 'Dried'), ('oil', 'Oil'), ('glycerite', 'Glycerite'), ('tea_blend', 'Tea blend'), ('fire_cider', 'Fire cider'), ('salve', 'Salve'), ('throat_spray', 'Throat spray'), ('wound_spray', 'Wound spray'), ('bitters', 'Bitters'), ('syrup', 'Syrup')], default='tincture', max_length=20)),
                ('herbs', models.ManyToManyField(to='inventory.Herb')),
            ],
        ),
        migrations.CreateModel(
            name='SimpleInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('tincture', 'Tincture'), ('dried', 'Dried'), ('oil', 'Oil'), ('glycerite', 'Glycerite'), ('tea_blend', 'Tea blend'), ('fire_cider', 'Fire cider'), ('salve', 'Salve'), ('throat_spray', 'Throat spray'), ('wound_spray', 'Wound spray'), ('bitters', 'Bitters'), ('syrup', 'Syrup')], default='tincture', max_length=20)),
                ('quantity', models.IntegerField()),
                ('herb', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Herb')),
            ],
        ),
        migrations.RemoveField(
            model_name='remedy',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='remedy',
            name='herbs',
        ),
        migrations.RemoveField(
            model_name='remedy',
            name='type',
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
        migrations.DeleteModel(
            name='PreparationType',
        ),
        migrations.DeleteModel(
            name='Remedy',
        ),
    ]