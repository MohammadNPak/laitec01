

from django.urls import path,include
from account import views
urlpatterns = [
    path('addeducation/',views.add_education,name='add_education' ),
    path('addexperience/',views.add_experience,name='add_experience' ),
    path('createprofile/',views.create_profile,name='create_profile' ),
    path('dashboard/',views.dashboard,name='dashboard' ),
    path('login/',views.login ,name='login' ),
    path('profile/<slug:username>/',views.profile,name='profile' ),
    path('profiles/',views.profiles,name='profiles' ),
    path('register/',views.register,name='register' ),
    ]
