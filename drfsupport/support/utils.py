from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from support.models import User


class UserSerializerMethods:
    """
    Методы для регистрации пользователя и валидации пароля
    """

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return make_password(value)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MessageViewSetMethods:
    """
    Методы для создания и получения сообщений
    """

    def retrieve(self, request, pk=None, ticket_pk=None):
        response = {'detail': 'Метод \"GET\" не разрешен.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception:
            return Response({'detail': 'Страница не найдена.'},
                            status=status.HTTP_404_NOT_FOUND)
