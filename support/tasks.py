from drfsupport.celery import app
from support.services import send_email_when_status_changed


@app.task
def send_email(ticket_title, ticket_status, client_email):
    send_email_when_status_changed(ticket_title, ticket_status, client_email)
