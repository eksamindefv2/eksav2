# Generated by Django 2.0.6 on 2018-08-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persediaan', '0008_auto_20180803_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soalan',
            name='NoSoalan',
            field=models.CharField(max_length=10, verbose_name='NoSoalan'),
        ),
    ]