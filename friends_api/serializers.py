from rest_framework import serializers
from .models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'name', 'age', 'is_close', 'meeting_date', 'notes', 'created_at', 'updated_at']