from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import GameRoom
from django.contrib.auth.models import User

@csrf_exempt
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

@csrf_exempt
def join_game_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        user_id = request.POST.get('user_id')

        if not room_name or not user_id:
            return JsonResponse({'error': 'Room name and user ID are required'}, status=400)

        try:
            room = GameRoom.objects.get(room_name=room_name)
        except GameRoom.DoesNotExist:
            return JsonResponse({'error': 'Game room does not exist'}, status=404)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        if room.players.count() >= 4:
            return JsonResponse({'error': 'Game room is full'}, status=400)

        room.players.add(user)
        return JsonResponse({'message': 'User added to game room successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

       
