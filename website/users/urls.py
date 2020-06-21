from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('medlogs/', views.medlogs, name="medlogs"),
    path('symptomlogs/', views.symptomlogs, name="symptomlogs"),
    path('medications/', views.medications, name="medications"),
    path('data/', views.data, name="data"),
    path('create_medlog/', views.createMedlog, name="create_medlog"),
    path('update_medlog/<str:pk>/', views.updateMedlog, name="update_medlog"),
    path('delete/<str:pk>/', views.deleteMedlog, name="delete_medlog"),
]
