# Generated by Django 2.0.6 on 2018-08-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0002_auto_20180718_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesi',
            name='Status',
            field=models.IntegerField(default=1, verbose_name='StatusSesi'),
        ),
    ]