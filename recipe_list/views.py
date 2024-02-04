from django.http import HttpResponseNotAllowed, JsonResponse
from rest_framework import status
from .models import User
from .encrypt import encrypt
from django.views.decorators.csrf import csrf_exempt
import uuid
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_info = json.loads(request.body)
        username = user_info['username']
        email = user_info['email']
        password = user_info['password']
        guid = str(uuid.uuid4())
        if not (username and email and password):
            return JsonResponse({'error': 'Username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        password = encrypt(password, guid)
        user = User(user_id=guid, username=username, email=email, password=password, is_active=False)
        user.save()
        return JsonResponse({'message': 'User successfully registered'}, status=status.HTTP_201_CREATED)
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def login(request):
    if request.method == 'POST':
        login_info = json.loads(request.body)
        username = login_info['username']
        password = login_info['password']
        if not (username and password):
            return JsonResponse({'error': 'username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist with this username'}, status=status.HTTP_400_BAD_REQUEST)
        password = encrypt(password, user.user_id)
        if user.password != password:
            return JsonResponse({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user.is_active = True
            user.save()
            return JsonResponse({'message': 'User successfully logged in'}, status=status.HTTP_200_OK)
    else:
        return HttpResponseNotAllowed(['POST'])
    
@csrf_exempt
def logout(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User-id is not correct'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        return JsonResponse({'message': 'User successfully logged out'}, status=status.HTTP_200_OK)
    else:
        return HttpResponseNotAllowed(['POST'])
