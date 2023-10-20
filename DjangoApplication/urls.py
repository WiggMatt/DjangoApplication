from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create_news', views.create_news, name='create_news'),
    path('more', views.more, name='more'),
    path('navbar', views.navbar, name='navbar'),
    path('news/<int:news_id>', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)