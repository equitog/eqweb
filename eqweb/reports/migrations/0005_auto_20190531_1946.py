# Generated by Django 2.2.1 on 2019-06-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20190531_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='id_subarea',
            field=models.ManyToManyField(help_text='Ingrese la subarea para la cuenta', to='reports.Subarea'),
        ),
    ]
