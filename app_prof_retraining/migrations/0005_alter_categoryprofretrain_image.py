# Generated by Django 4.1.7 on 2023-09-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_retraining', '0004_categoryprofretrain_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryprofretrain',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='prof_retr/category_img/'),
        ),
    ]