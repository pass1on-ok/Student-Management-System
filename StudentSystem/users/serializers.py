from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role')