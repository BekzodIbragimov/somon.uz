from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search_house', views.search_house, name='search_house'),
    
]
