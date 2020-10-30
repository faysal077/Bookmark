
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import user_Login
urlpatterns = [
    #path('login/', views.user_Login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.dashboard,name='dashboard'),
]
