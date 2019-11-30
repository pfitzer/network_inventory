import pytest
from mixer.backend.django import mixer

from django.test import Client
from django.contrib.auth import get_user_model

import helper

pytestmark = pytest.mark.django_db


def test_computer_detail_view_not_logged_in():
    response = Client().get('/computer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/230/')
    assert response.status_code == 404


def test_computer_detail_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, computer.name))


def test_computer_detail_view_no_permissions():
    User = get_user_model()
    User.objects.create_user("novartis-admin", "admin@novartis.com",
                             "password", is_staff=True)
    client = Client()
    mixer.blend('inventory.Customer')
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert response.status_code == 403
