from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create_news', views.create_news, name='create_news'),
    path('more', views.more, name='more'),
    path('navbar', views.navbar, name='navbar'),
    path('news/<int:news_id>', views.news_detail, name='news_detail'),
    path('news/<int:news_id>/update', views.news_update, name='news_update'),
    path('news/<int:news_id>/delete', views.news_delete, name='news_delete'),
]

