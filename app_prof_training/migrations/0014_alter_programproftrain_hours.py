# Generated by Django 4.2.6 on 2023-11-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prof_training', '0013_alter_categoryproftrain_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programproftrain',
            name='hours',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]