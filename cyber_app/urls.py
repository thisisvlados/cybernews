from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]
