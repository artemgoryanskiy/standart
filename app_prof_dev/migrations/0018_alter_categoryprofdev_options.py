# Generated by Django 4.2.6 on 2023-10-12 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_dev', '0017_alter_categoryprofdev_purpose'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryprofdev',
            options={'ordering': ['pk']},
        ),
    ]
