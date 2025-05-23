from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import sample_api


urlpatterns = [
    
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name= 'logout'),
    
    path("api/sample/", sample_api, name="sample_api"),

]
