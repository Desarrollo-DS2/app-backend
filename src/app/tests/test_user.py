from . import general_setup
import pytest
from ..models.user_model import User


@pytest.fixture
def test_user():
    email = 'prueba@gmail.com'
    user_id = '10101010'
    first_name = 'Prueba'
    last_name = 'Prueba'
    password = 'password123'

    if not User.objects.filter(email=email).exists():
        user = User.objects.create(
            email=email, user_id=user_id, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

    yield User.objects.get(email=email)

    User.objects.get(email=email).delete()


def test_user_email(test_user):
    assert test_user.get_email() == 'prueba@gmail.com'


def test_user_user_id(test_user):
    assert test_user.get_user_id() == '10101010'


def test_user_first_name(test_user):
    assert test_user.get_first_name() == 'Prueba'


def test_user_last_name(test_user):
    assert test_user.get_last_name() == 'Prueba'
