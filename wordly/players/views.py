from django.shortcuts import redirect
from rest_framework import mixins, viewsets
from rest_framework.serializers import ValidationError

from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, *args, **kwargs):
        """Поиск или создание игрока"""
        if 'username' not in request.data:
            raise ValidationError(
                'Нет ключа username'
            )
        username = request.data['username']
        player = Player.objects.filter(username=username)
        if player:
            """Если игрок существует, перенаправляем на игру или её создание"""
            lobby = player[0].lobby_id
            if lobby:
                return redirect(
                    f'lobby/{username}/{lobby}/',
                    permanent=True
                )
            return redirect(
                f'lobby/{username}/',
                permanent=True
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return redirect(
            f'lobby/{username}/',
            permanent=True
        )
