from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):

  return render(request,
                  'blog/dashboard.html',
                  context={"name":"mohammad","is_auth":True }
                )