from django.shortcuts import render
from django.http import JsonResponse
from .models import GameRoom

def create_game_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        
        if not room_name:
            return JsonResponse({'error': 'Room name is required'}, status=400)

        if GameRoom.objects.filter(room_name=room_name).exists():
            return JsonResponse({'error': 'Room name already exists'}, status=400)
        
        room = GameRoom.objects.create(room_name=room_name)
        return JsonResponse({'message': 'Game room created successfully', 'room_id': room.id})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
