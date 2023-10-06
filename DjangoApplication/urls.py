
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('more', views.more, name='more'),
    path('navbar', views.navbar, name='navbar'),
]
