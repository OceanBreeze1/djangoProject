from django.urls import path
from apps.views import HomeView,IndexView,ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about', IndexView.as_view(), name='about'),
    path('contacts', ContactView.as_view(), name='contact'),
    path('menu', ContactView.as_view(), name='menu'),
    path('news', ContactView.as_view(), name='news'),
    path('news_detail', ContactView.as_view(), name='news_detail')


    ]

