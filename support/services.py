from django.core.mail import send_mail

from drfsupport.settings import DEFAULT_FROM_EMAIL


def send_email_when_status_changed(ticket_title, ticket_status, client_email):
    send_mail(
        subject='Статус тикета изменён.',
        message=f"Статус вашего тикета '{ticket_title}' был изменен на {ticket_status}.",
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[client_email],
        fail_silently=False,
    )
