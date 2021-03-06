from django.urls import path
from . import views

urlpatterns = [

     path('', views.index, name='index'),
     path('about', views.about, name='about'),
     path('login', views.login, name='login'),
     path('register', views.register, name='register'),
     path('logout', views.logout, name='logout'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('profile', views.profile, name='profile'),
     path('contact', views.contact, name='contact'),

]