from .models import board_api
from rest_framework import serializers

class Board_apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = board_api
        fields = ['title', 'body', 'created_at', 'updated_at']
