# Generated by Django 4.1.7 on 2023-09-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_dev', '0008_categoryprofdev_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryprofdev',
            name='short_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
