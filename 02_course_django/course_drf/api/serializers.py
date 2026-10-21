from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'todo',
            'description',
            'completed',
            'created_at',
        ]
        read_only_fields = ['created_at']