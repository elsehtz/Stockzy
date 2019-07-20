from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('settings', views.settings, name = 'settings'),
    path('ayo', views.ayo_home, name = "ayo_home"),
    path('add', views.add, name = 'add')
]