# Generated by Django 3.2 on 2021-05-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICT4D_prototype', '0005_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='cercle_num',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='chosen_language',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='rec_commune',
            field=models.FileField(default=2, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='rec_location',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='rec_name',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='tree_count',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='tree_num',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
