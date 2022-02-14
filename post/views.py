from urllib import response
from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def test(request):
    return HttpResponse("hello world")
def post(requst):
    return render(requst, 'post/post.html') 
       
