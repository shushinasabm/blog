# Generated by Django 4.0.2 on 2022-02-14 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('discription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uppdated_at', models.DateTimeField(auto_now=True)),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1)),
            ],
        ),
    ]
