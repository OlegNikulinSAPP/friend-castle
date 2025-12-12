from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Friend
from .serializers import FriendSerializer


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