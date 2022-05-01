from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from support.models import Message, Ticket, User
from support.serializers import (MessageSerializer, TicketSerializer,
                                 UserRegistrationSerializer)
from support.utils import MessageViewSetMethods


class TicketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    Тикеты
    Клиент может создавать и просматривать свои созданные тикеты
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.all().filter(client=self.request.user)


class MessageViewSet(MessageViewSetMethods,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    Сообщения тикета
    Клиент может писать сообщение саппорту и просматривать все сообщения
    """

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(ticket=self.kwargs['ticket_pk'])

    def perform_create(self, serializer):
        serializer.save(ticket_id=self.kwargs.get('ticket_pk'),
                        sender=self.request.user,
                        receiver=User.objects.get(is_superuser=True))


class UserRegistrationViewSet(viewsets.ModelViewSet):
    """
    Регистрация пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
