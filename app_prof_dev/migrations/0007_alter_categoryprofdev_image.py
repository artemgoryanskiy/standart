# Generated by Django 4.1.7 on 2023-09-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_dev', '0006_rename_category_categoryprofdev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryprofdev',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='prof_dev/category_img/'),
        ),
    ]
