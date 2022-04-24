from django.shortcuts import render

# Create your views here.

def add_education(request):
    return render(request,'account/add-education.html',context={})


def add_experience(request):

    return render(request,'account/add-experience.html',context={})


def create_profile(request):
    return render(request,'account/create-profile.html',context={})


def dashboard(request):
    user ={"is_authenticated":False}
    return render(request,'account/dashboard.html',context={"user":1})


def login(request):
    return render(request,'account/login.html',context={})


def profile(request):
    return render(request,'account/profile.html',context={})

def profiles(request):
    return render(request,'account/profiles.html',context={})

def register(request):
    return render(request,'account/register.html',context={})
