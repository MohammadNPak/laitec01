from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def add_education(request):
    return render(request,'blog/add-education.html',context={})

def add_experience(request):
    return render(request,'blog/add-experience.html',context={})

def create_profile(request):
    return render(request,'blog/create-profile.html',context={})

def dashboard(request):
    return render(request,'blog/dashboard.html',context={})

def index(request):
    return render(request,'blog/index.html',context={})

def login(request):
    return render(request,'blog/loginn.html',context={})

def post(request):
    return render(request,'blog/post.html',context={})

def posts(request):
    return render(request,'blog/posts.html',context={"name":"Jafar","is_auth":True})

def profile(request):
    return render(request,'blog/profile.html',context={"name":"Jafar","is_auth":True})

def profiles(request):
    return render(request,'blog/profiles.html',context={"name":"Jafar","is_auth":True})

def register(request):
    return render(request,'blog/register.html',context={})
