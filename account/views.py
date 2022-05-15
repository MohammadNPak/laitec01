from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import UserProfile

# Create your views here.


user = {}
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


def profile(request,username):

    user_profile = (UserProfile.objects
                    .select_related('user')
                    .get(user__username=username))

    return render(request,'account/profile.html',context={"user_profile":user_profile})

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
