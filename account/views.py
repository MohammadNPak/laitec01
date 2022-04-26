from multiprocessing import context
from django.shortcuts import render

# Create your views here.

user = {
    "is_authenticated":True,
    "first_name":"jhon",
    "last_name":"doe",
    "email":"jhondoe@gmail.com",
    "phone":"+1-123-456-7890",
    "address":"123, Main Street, New York, NY, USA",
    "city":"new york",
    "state":"new york",
    "zip":"12345",
    "country":"usa",
    "profile_image":"img/profile-image.png",
    "cover_image":"img/cover-image.png",
    "bio":"im a web developer and i love to code",
    "website":"showmeyourcode.ir",
    "skills":"python, django, javascript, html, css",
    "education":['Bachelor of Science in Computer Science','University of California, Los Angeles','California, USA'],
    "experience":["2 years of experience in web development","1 year of experience in web development","1 year of experience in web development"],

}


def add_education(request):
    context = {
        "user":user
    }
    return render(request,'account/add-education.html',context=context)


def add_experience(request):
    context = {
        "user":user
    }
    return render(request,'account/add-experience.html',context=context)


def create_profile(request):
    context = {
        "user":user
    }
    return render(request,'account/create-profile.html',context=context)


def dashboard(request):
    context = {
        "user":user
    }
    return render(request,'account/dashboard.html',context=context)


def login(request):
    context = {
        "user":user
    }
    return render(request,'account/login.html',context=context)


def profile(request):
    context = {
        "user":user
    }
    return render(request,'account/profile.html',context=context)

def profiles(request):
    context = {
        "user":user
    }
    return render(request,'account/profiles.html',context=context)

def register(request):
    context = {
        "user":user
    }
    return render(request,'account/register.html',context=context)
