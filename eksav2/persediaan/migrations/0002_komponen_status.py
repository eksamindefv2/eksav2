# Generated by Django 2.0.6 on 2018-08-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persediaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='komponen',
            name='Status',
            field=models.IntegerField(default=1, verbose_name='Status'),
        ),
    ]