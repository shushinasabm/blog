from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render , get_object_or_404
from django.http import  HttpResponse
from .models import Post
# Create your views here.
def index (request):
    return render(request ,'post/index.html')
def aboutus (request):
    return render(request ,'post/aboutus.html')
def contactus (request):
    return render(request ,'post/contactus.html')
    
def test(request):
    #دستور برگشت هر استیرینگی
    return HttpResponse("hello world")
def posts(requst):
    #دستور برگشت خواندن همه اطلاعات از دل پست
    posts =Post.objects.filter(status = 'p').order_by("-publish_at")
    # print(posts)   
    context = {
        "posts":posts
    }
    #دستورات رو از مدل گرفتیم و میخوایم به تملیت بدیم
    return render(requst, 'post/post.html', context) 
def detail(request ,slug ):
     context ={
         'post':get_object_or_404(Post,slug = slug , status='p')
     }
     return render(request , "post/detail.html", context)

       
