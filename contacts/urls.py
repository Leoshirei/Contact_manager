from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_site, name = 'home'),
    path('register/', views.register_site, name = 'register'),
    path('login/', views.login_site, name = 'login'),
    path('logout/', views.logout_site, name = 'logout'),
    path('main_panel/', views.main_panel, name = 'main_panel'),
    path('create_contact/', views.create_contact, name = 'create_contact'),
]