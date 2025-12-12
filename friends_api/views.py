from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Friend


@api_view(['GET'])
def friend_list(request):
    """
    Получить список всех друзей.
    """
    friends = Friend.objects.all()
    # Пока вернём просто имена
    data = [{'name': friend.name} for friend in friends]
    return Response(data)
