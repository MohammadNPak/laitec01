
from django.contrib import admin
from django.urls import path,include
from blog import urls as blog_urls
from blog.views import index
from account import urls as account_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include(blog_urls)),
    path('account/',include(account_url)),
    path('',index,name="index"),
]
