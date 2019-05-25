from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'rcs-users'
urlpatterns = [
    path('home', views.Home.as_view(), name="home"),
    path('users/', views.Home.as_view(), name='user_list'),
    path('users/add/type/', views.user_type, name='add_user_type'),
    path('user/add/error/page/',views.error_page, name='error_page'),
    path('users/add/role/', views.role_center, name='add_user_role'),
    path('citizen/config/', views.citizen_config, name='add_a_citizen'),
    path('agent/config/', views.agent_config, name='add_an_agent'),
    path('<int:pk>/', views.UpdateView.as_view(), name='user_details'),
    path('register/', views.register, name='register-user'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html' ), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view( template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view( template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view( template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
]
