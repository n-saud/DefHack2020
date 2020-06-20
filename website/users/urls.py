from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logs/', views.logs, name="logs"),
    path('medications/', views.medications, name="medications"),
    path('data/', views.data, name="data"),
]
