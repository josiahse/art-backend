# Generated by Django 4.0 on 2021-12-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
        migrations.AlterField(
            model_name='color',
            name='color_list',
            field=models.CharField(max_length=15000),
        ),
    ]