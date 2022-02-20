

from django.db import models

from django.utils import timezone

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES =(
    ('d', 'Draft'),('p','Publish'),

    )
    #اطلاعاتی که مربوط به پست هامونه یک سری دیتا برای دریافت داره که در زیر مینویسیم 
    title = models.CharField(max_length=100,blank=False)
    slug = models.SlugField(max_length=30,unique=True)
    discription = models.TextField()
    thumbnail = models.ImageField(upload_to='images/',null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    uppdated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(default=timezone.now)
    status =models.CharField(max_length=1,choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.title

class aboutus(models.Model):

    title_us = models.CharField(max_length=100,blank=False)
    Discrepant_us = models.TextField()
    insta_us = models.URLField(max_length=200)
    git_hub_us =models.URLField(max_length=200)
    thumbnail_us = models.ImageField(upload_to='images/',null=True)
    phone_us =models.CharField(max_length=14)
    tiwtter_us =models.URLField(max_length=200)
    address_us=models.CharField(max_length=200)
    email_us =models.CharField(max_length=200)
    linkedin_us =models.URLField(max_length=200)
    facebook_us =models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.title_us        