# Generated by Django 4.1.7 on 2023-08-15 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lab_prot', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductLabProt',
        ),
    ]
