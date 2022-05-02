from rest_framework import serializers

from support.models import Message, Ticket, User
from support.utils import UserSerializerMethods


class TicketSerializer(serializers.ModelSerializer):
    """
    Сериализатор тикетов для клиента
    """

    time_create = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    time_update = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = ['id', 'client', 'title', 'content', 'status', 'time_create', 'time_update']
        read_only_fields = ['status']


class MessageSerializer(serializers.ModelSerializer):
    """
    Сериализатор сообщений для клиента
    """

    ticket = serializers.ReadOnlyField(source='ticket.title')
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    time_create = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Message
        fields = ['ticket', 'text', 'time_create', 'sender', 'receiver']


class UserRegistrationSerializer(serializers.ModelSerializer, UserSerializerMethods):
    """
    Сериализатор регистрации для клиента
    """

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
