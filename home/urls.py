from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
<<<<<<< HEAD
    path('search_house', views.search_house, name='search_house'),
    
=======
    path('home_detail/<detail_id>', views.post, name='post-detail'),
>>>>>>> 1d4d21a8b8a50eebdb0b5b3d659410afd9d68b40
]
    
