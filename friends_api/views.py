from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Friend
from .serializers import FriendSerializer
from django.shortcuts import render, redirect


@api_view(['GET', 'POST'])
def friend_list(request):
    if request.method == 'GET':
        friends = Friend.objects.all()
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("Получены данные:", request.data)  # Для отладки
        serializer = FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def friend_create_form(request):
    """Показывает форму для добавления друга и обрабатывает её"""
    if request.method == 'POST':
        # 1. Собираем данные из формы
        name = request.POST.get('name')
        age = request.POST.get('age')
        is_close = bool(request.POST.get('is_close'))  # 'on' или None

        print(f"Получены данные: имя={name}, возраст={age}, близкий={is_close}")

        # 2. Сохраняем друга в базу (пока без валидации)
        friend = Friend.objects.create(
            name=name,
            age=age if age else None,  # Если возраст пустой - ставим None
            is_close=is_close
        )

        print(f"Создан друг: {friend.name}")

        # 3. Перенаправляем на список друзей
        return redirect('friend-list-api')

    # Если GET-запрос - просто показываем форму
    return render(request, 'friends_api/friend_form.html')
