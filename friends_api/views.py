from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Friend
from .serializers import FriendSerializer  # ← Импортируем сериализатор!

@api_view(['GET'])
def friend_list(request):
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)  # ← Используем сериализатор
    return Response(serializer.data)
