
from django.urls import path
from blog import views
urlpatterns = [
    path('post/<slug:slug>',views.post,name='post'),
    path('posts/',views.posts,name='posts'),

]