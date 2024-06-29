from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='grievances/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('submit/', views.submit_grievance, name='submit_grievance'),
    path('grievance_list/', views.grievance_list, name='grievance_list'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.grievance_detail, name='grievance_detail'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
