from django.contrib.auth.models import AbstractUser
from django.db import models

from support.tasks import send_email


class User(AbstractUser):
    """Модель пользователей"""

    class Meta:
        ordering = ['id']
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'


class Ticket(models.Model):
    """Модель тикетов"""

    title = models.CharField(max_length=255, verbose_name='Название тикета')
    content = models.TextField(verbose_name='Контент тикета')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент, создавший тикет')

    SOLVED = 'SOLVED'
    UNSOLVED = 'UNSOLVED'
    FROZEN = 'FROZEN'

    STATUS_CHOICES = [
        (UNSOLVED, 'SOLVED'),
        (SOLVED, 'UNSOLVED'),
        (FROZEN, 'FROZEN'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0],
        verbose_name='Статус тикета',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'тикет'
        verbose_name_plural = 'Тикеты'

    def __str__(self):
        return self.title

    __old_status = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status != self.__old_status:
            send_email.delay(self.title, self.status, self.client.email)

        super().save(force_insert, force_update, *args, **kwargs)
        self.__original_name = self.status


class Message(models.Model):
    """Модель сообщений"""

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Название тикета')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Отправитель сообщения', related_name='message_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 verbose_name='Получатель сообщения', related_name='message_receiver')
    text = models.TextField(verbose_name='Cообщениe')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки сообщения')

    class Meta:
        ordering = ['id']
        verbose_name = 'сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.ticket
