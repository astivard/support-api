import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        username='client_1',
        email='client_1@gmail.com',
        password='client_1_password',
    )
    response = client.post('/api/v1/registration/', payload)
    data = response.data

    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert 'password' not in data
    assert response.status_code == 201
    assert len(data) == 2


@pytest.mark.django_db
def test_ticket_creation_for_unauthorized_user(client):
    payload = dict(
        title='Problem with registration!',
        content='Hello, I have a problem with my registration.',
    )
    response = client.post('/api/v1/tickets/', payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_ticket_creation_for_authorized_user(auth_client):
    payload = dict(
        title='Problem with registration!',
        content='Hey, I have a problem with my registration.',
    )

    response = auth_client.post('/api/v1/tickets/', payload)
    data = response.data

    assert data['title'] == payload['title']
    assert data['content'] == payload['content']
    assert response.status_code == 201
    assert len(data) == 6


@pytest.mark.django_db
def test_ticket_list_for_user(auth_client):
    response = auth_client.get('/api/v1/tickets/')
    assert response.status_code == 200
