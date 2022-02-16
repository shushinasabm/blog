

from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post
# Create your views here.
def test(request):
    #دستور برگشت هر استیرینگی
    return HttpResponse("hello world")
def post(requst):
    #دستور برگشت خواندن همه اطلاعات از دل پست
    posts =Post.objects.all()
    # print(posts)   
    context = {
        "posts":posts
    }
    #دستورات رو از مدل گرفتیم و میخوایم به تملیت بدیم
    return render(requst, 'post/post.html', context) 

       
