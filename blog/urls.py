
from django.urls import path
from blog import views
urlpatterns = [
    path('post/',views.post,name='post'),
    path('posts/',views.posts,name='posts'),
    path('index/',views.index,name='index' ),

]