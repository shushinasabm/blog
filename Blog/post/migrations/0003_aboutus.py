# Generated by Django 4.0.2 on 2022-02-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='images/')),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('address', models.TextField(null=True)),
                ('email', models.EmailField(max_length=200)),
                ('linkedIn', models.URLField()),
                ('github', models.URLField()),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
            ],
        ),
    ]