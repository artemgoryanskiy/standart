# Generated by Django 4.1.7 on 2023-09-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_training', '0008_categoryproftrain_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproftrain',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='prof_train/category_img/'),
        ),
    ]