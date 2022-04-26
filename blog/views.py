from django.http import HttpResponse
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


def index(request):
    context = {
        "user":user}
    
    return render(request,'blog/index.html',context=context)

def post(request):
    context = {
        "user":user}
    
    
    return render(request,'blog/post.html',context=context)

def posts(request):
    context = {
        "user":user}
    return render(request,'blog/posts.html',context=context)



