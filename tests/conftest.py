import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from support.models import User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(client):
    user = User.objects.create_user(username='client_1', email='client_1@gmail.com', password='Fdfdg23GDDF32fdsf23g2d3')
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client
