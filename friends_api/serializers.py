# friends_api/serializers.py
from rest_framework import serializers
from .models import Hobby, Friend, Meeting


class HobbySerializer(serializers.ModelSerializer):
    """Переводчик для увлечений 🎭"""

    class Meta:
        model = Hobby  # 👈 Говорим: "Переводи с языка модели Hobby"
        fields = ['id', 'name', 'description', 'created_at']  # 👈 Какие поля переводить
        read_only_fields = ['id', 'created_at']  # 👈 Эти поля только для чтения