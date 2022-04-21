from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, 'blog/dashboard.html', context={})


def add_education(request):
    return render(request, 'blog/add-education.html', context={})


def add_experience(request):
    return render(request, 'blog/add-experience.html', context={})

def create_profile(request):
    return render(request, 'blog/create-profile.html', context={})

def index(request):
    return render(request, 'blog/index.html', context={})