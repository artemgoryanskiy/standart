# Generated by Django 4.1.7 on 2023-08-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_training', '0006_rename_category_categoryproftrain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programproftrain',
            name='class_num',
            field=models.CharField(max_length=50),
        ),
    ]
