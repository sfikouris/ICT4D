# Generated by Django 3.2 on 2021-05-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICT4D_prototype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='treeaid_databese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cercle', models.CharField(max_length=100)),
                ('tree', models.CharField(max_length=100)),
                ('tree_count', models.IntegerField()),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='treeaid',
        ),
    ]
