# Generated by Django 4.0.2 on 2022-02-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_us', models.CharField(max_length=100)),
                ('Discrepant_us', models.TextField()),
                ('insta_us', models.URLField()),
                ('git_hub_us', models.URLField()),
                ('thumbnail_us', models.ImageField(null=True, upload_to='images/')),
                ('phone_us', models.CharField(max_length=14)),
                ('tiwtter_us', models.URLField()),
                ('address_us', models.CharField(max_length=200)),
                ('email_us', models.CharField(max_length=200)),
                ('linkedin_us', models.URLField()),
                ('facebook_us', models.URLField()),
            ],
        ),
    ]