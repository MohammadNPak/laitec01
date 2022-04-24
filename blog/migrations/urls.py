from django.urls import path
from blog import views
urlpatterns = [
    path('add-education/',views.add_education),
    path('add-experience/',views.add_experience),
    path('create-profile/',views.create_profile),
    path('dashboard/',views.dashboard),
    path('index/',views.index),
    path('login/',views.login),
    path('post/',views.post),
    path('posts/',views.posts),
    path('profile/',views.profile),
    path('profiles/',views.profiles),
    path('register/',views.register)
]
