# Generated by Django 3.2 on 2022-01-18 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0008_delete_productreview'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='ProductReview',
        ),
    ]
