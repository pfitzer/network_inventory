import pytest
from mixer.backend.django import mixer

from django.test import Client

import helper

pytestmark = pytest.mark.django_db


def test_user_detail_view_not_logged_in():
    response = Client().get('/user/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_user_detail_view(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, user))


def test_user_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/230/')
    assert response.status_code == 404


def test_user_detail_view_ad_group(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    group = mixer.blend('inventory.AdGroup')
    mixer.blend('inventory.UserInAdGroup', user=user, group=group)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "AD Groups"))


def test_user_detail_view_mail_group(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    group = mixer.blend('inventory.MailGroup')
    mixer.blend('inventory.UserInMailGroup', user=user, group=group)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "Mail Groups"))


def test_user_detail_view_mail_alias(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    mixer.blend('inventory.MailAlias', user=user)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "Mail Alias"))


def test_user_detail_view_license(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    mixer.blend('inventory.UserLicense', software=mixer.SELECT)
    mixer.blend('inventory.LicenseWithUser', user=user)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "License"))


def test_user_detail_view_computer(create_admin_user):
    create_admin_user()
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    computer = mixer.blend('inventory.Computer', user=user)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, computer))


def test_user_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend('inventory.Customer')
    user = mixer.blend('inventory.User', customer=customer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/user/' + str(user.id) + '/')
    assert response.status_code == 403

