# Generated by Django 3.2 on 2022-01-24 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]
