# grievances/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('submit/', views.submit_grievance, name='submit_grievance'),
    path('grievance_list/', views.grievance_list, name='grievance_list'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.grievance_detail, name='grievance_detail'),
]
