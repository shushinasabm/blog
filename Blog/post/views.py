
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import AboutUs, Post
# Create your views here.


def aboutUs(request):
    context = {
        'aboutus':AboutUs.objects.first()
    }
    return render(request,'post/about-us.html',context=context)

def contactUs(request):
    return render(request,'post/contact-us.html')
def index(request):
    #دستور خواندن همه اطلاعات از مدل پست
    posts = Post.objects.filter(status = 'p').order_by('-published_at')
    
    # print(posts)
    context = {
        "posts":posts
    }
    return render(request,'post/base.html',context=context)

def detail(request , slug):
    context = {
        'post': get_object_or_404(Post, slug = slug , status='p')
    }
    return render(request , "post/detail.html", context)