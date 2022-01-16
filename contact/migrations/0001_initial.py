# Generated by Django 3.2 on 2022-01-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(choices=[('general_query', 'GENERAL QUERY'), ('update_cancel_my_order', 'UPDATE OR CANCEL MY ORDER'), ('sign_in_or_sign_up_issue', 'SIGN IN OR SIGN UP ISSUE'), ('offer_your_products', 'OFFER YOUR PRODUCTS')], default='general_query', max_length=100)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
