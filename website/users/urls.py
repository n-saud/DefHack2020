from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('my_heros/', views.friends, name="friends"),
    path('achievements/', views.achievements, name="achievements"),

    path('medlogs/', views.medlogs, name="medlogs"),
    path('medreminders/', views.medReminders, name="medreminders"),
    path('symptomlogs/', views.symptomlogs, name="symptomlogs"),
    path('medications/', views.medications, name="medications"),
    path('data/', views.data, name="data"),

    path('create_medlog/', views.createMedlog, name="create_medlog"),
    path('update_medlog/<str:pk>/', views.updateMedlog, name="update_medlog"),
    path('delete_medlog/<str:pk>/', views.deleteMedlog, name="delete_medlog"),

    path('add_symptom/', views.addSymptom, name="add_symptom"),
    path('create_symptomlog/', views.createSymptomLog, name="create_symptomlog"),
    path('update_symptomlog/<str:pk>/', views.updateSymptomlog, name="update_symptomlog"),
    path('delete_symptomlog/<str:pk>/', views.deleteSymptomlog, name="delete_symptomlog"),

    path('create_medication/', views.createMedication, name="create_medication"),
    path('update_medication/<str:pk>/', views.updateMedication, name="update_medication"),
    path('delete_medication/<str:pk>/', views.deleteMedication, name="delete_medication"),
]
