from rest_framework import serializers
from .models import GameApp

class GameAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameApp
        fields = '__all__'