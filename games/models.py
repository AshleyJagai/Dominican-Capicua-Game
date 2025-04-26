from django.db import models
from django.contrib.auth.models import User

class GameRoom(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    players = models.ManyToManyField(User, related_name="game_rooms")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name

