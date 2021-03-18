# Generated by Django 2.2.19 on 2021-03-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210314_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='units',
            field=models.CharField(choices=[('ounces', 'ounces'), ('1_oz_jar', '1 oz jars'), ('2_oz_jar', '2 oz jars'), ('4_oz_jar', '4 oz jars')], default='ounces', max_length=20),
        ),
    ]