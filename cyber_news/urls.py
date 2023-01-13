from django.urls import path, re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.news, name='news'),
    path('dota/', views.news_dota, name='news_dota'),
    path('csgo/', views.news_csgo, name='news_csgo'),
    path('pubg/', views.news_pubg, name='news_pubg'),
    path('valorant/', views.news_valorant, name='news_valorant'),
    path('create/', views.news_create, name='news_create'),
    path('<int:pk>/', views.NewsDetailView, name='news_detail'),
    path('<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/like/', views.AddLike, name='like'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)