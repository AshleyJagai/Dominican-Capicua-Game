from django.urls import path
from .views import create_game_room, join_game_room

urlpatterns = [
    path('create/', create_game_room, name='create_game_room'),
    path('join/', join_game_room, name='join_game_room'),
]

