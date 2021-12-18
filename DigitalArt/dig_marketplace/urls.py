from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_page, name="logout_page"),
    path('account/', views.account_page, name='account'),
]