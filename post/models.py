from django.db import models
from django.utils import timezone
#* Post Models
class Post(models.Model):
    STATUS_CHOICES =(
        ('d','Draft'),
        ('p','Publish'),
    )
    title = models.CharField(max_length=100,blank=False)
    slug = models.SlugField(max_length=30,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/',null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)


    def __str__(self) -> str:
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=30, null=True, blank=False)
    description = models.TextField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length= 11, blank=True)
    address = models.TextField(null=True, blank=False)
    email = models.EmailField(max_length=200)
    linkedIn = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.title


