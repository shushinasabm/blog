

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


        