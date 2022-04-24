from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'blog/index.html',context={})

def post(request):
    return render(request,'blog/post.html',context={})

def posts(request):
    return render(request,'blog/posts.html',context={"name":"Jafar","is_auth":True})



