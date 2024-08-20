from rest_framework import generics
from users.serializers import UserSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания пользователя
    """
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.is_active == ('True')
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
