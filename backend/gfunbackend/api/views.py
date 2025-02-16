from rest_framework import status
from rest_framework import generics
from .models import GameApp
from .serializers import GameAppSerializer

class GameList(generics.ListAPIView):
    queryset = GameApp.objects.all()
    serializer_class = GameAppSerializer