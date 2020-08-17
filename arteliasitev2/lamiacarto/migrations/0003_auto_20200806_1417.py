# Generated by Django 3.0.8 on 2020-08-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamiacarto', '0002_auto_20200803_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='id_projet',
            new_name='id_project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='nom',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='postgisdb',
        ),
        migrations.RemoveField(
            model_name='project',
            name='postgispw',
        ),
        migrations.RemoveField(
            model_name='project',
            name='postgisuser',
        ),
        migrations.AddField(
            model_name='project',
            name='pgdbname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='pghost',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='pgpassword',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='pgport',
            field=models.IntegerField(blank=True, default=8080),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='pgschema',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='pguser',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='qgisserverurl',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
