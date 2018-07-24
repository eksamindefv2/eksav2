# Generated by Django 2.0.6 on 2018-07-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persediaan', '0001_initial'),
        ('urusetia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BilJadual', models.IntegerField(unique=True, verbose_name='BilJadual')),
                ('NamaJuruAudit', models.CharField(max_length=60, verbose_name='NamaJuruAudit')),
                ('TarikhAudit', models.DateTimeField(max_length=60, verbose_name='TarikhAudit')),
                ('Status', models.CharField(max_length=60, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Komen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KomenID', models.IntegerField(unique=True, verbose_name='KomenID')),
                ('Deskripsi', models.CharField(max_length=200, verbose_name='Deskripsi')),
                ('TarikhKomen', models.DateTimeField(max_length=60, verbose_name='TarikhKomen')),
                ('ICNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urusetia.Peranan')),
            ],
        ),
        migrations.CreateModel(
            name='Sesi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BilSesi', models.IntegerField(unique=True, verbose_name='BilSesi')),
                ('Tahun', models.IntegerField(verbose_name='Tahun')),
                ('TarikhMula', models.DateField(max_length=60, verbose_name='TarikhMula')),
                ('TarikhTamat', models.DateField(max_length=60, verbose_name='TarikhTamat')),
                ('Status', models.CharField(max_length=60, verbose_name='TarikhTamat')),
                ('TarikhKemaskini', models.DateTimeField(max_length=60, verbose_name='TarikhKemaskini')),
            ],
        ),
        migrations.CreateModel(
            name='Skor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BilMarkah', models.IntegerField(unique=True, verbose_name='BilMarkah')),
                ('Markah', models.IntegerField(verbose_name='Markah')),
                ('TarikhSkor', models.DateTimeField(max_length=60, verbose_name='TarikhSkor')),
                ('Catatan', models.CharField(max_length=200, verbose_name='Catatan')),
                ('ICNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urusetia.Peranan')),
                ('KomenID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penilaian.Komen')),
                ('NoJawapan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persediaan.Jawapan')),
                ('NoSoalan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persediaan.Soalan')),
            ],
        ),
        migrations.AddField(
            model_name='jadual',
            name='BilSesi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penilaian.Sesi'),
        ),
        migrations.AddField(
            model_name='jadual',
            name='IDZon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urusetia.Zon'),
        ),
    ]