# Generated by Django 3.2 on 2021-05-11 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ICT4D_prototype', '0012_remove_treeaid_dummy_rec'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='src_commune',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='src_location',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='src_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='treeaid',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='rec_commune',
            field=models.FileField(null=True, upload_to='commune/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='rec_location',
            field=models.FileField(null=True, upload_to='location/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='rec_name',
            field=models.FileField(null=True, upload_to='name/'),
        ),
    ]