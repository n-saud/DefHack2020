from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.register),
    path('logs/', views.logs),
    path('medications/', views.medications),
    path('data/', views.data),
]
