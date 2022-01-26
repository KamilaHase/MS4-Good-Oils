# Generated by Django 3.2 on 2022-01-25 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('author', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('article', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='magazine.magazine')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_desc', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='magazine.post')),
            ],
        ),
    ]