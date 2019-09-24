import pytest
from mixer.backend.django import mixer

from django.test import Client

from helper import in_content, not_in_content

pytestmark=pytest.mark.django_db

def test_customer_backup_table_not_logged_in():
    response = Client().get('/customer/1/backups/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_backup_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    backup = mixer.blend('inventory.Backup', customer=mixer.SELECT)
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert response.status_code == 200 and in_content(response, backup.name)


def test_customer_backup_table_no_backup(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert response.status_code == 200 and not_in_content(response, "Novartis PC")
