from django.urls import path
from . import views
from .views import UserListView,LogListView,UserActivityReportView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
   
    path('users/', UserListView.as_view(), name='user-list'),
    path('logs/', LogListView.as_view(), name='log-list'),
    path('user-activity/', UserActivityReportView.as_view(), name='report-list'),
    path('user-report/<int:user_id>/', views.user_report, name='user-report'),


]
