# Generated by Django 4.1.7 on 2023-08-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='ecology_img/')),
            ],
        ),
    ]
