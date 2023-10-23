# Generated by Django 4.2.6 on 2023-10-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutor',
            options={'ordering': ['last_name']},
        ),
        migrations.AddField(
            model_name='tutor',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='vk_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
