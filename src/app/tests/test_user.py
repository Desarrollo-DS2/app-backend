from . import test_setup
import pytest
from ..models.user_model import User
import datetime


@pytest.fixture
def test_user():
    email = 'prueba@gmail.com'
    user_id = '10101010'
    first_name = 'Prueba'
    last_name = 'Prueba'
    password = 'password123'
    second_last_name = 'Prueba'
    contact_number = '1234567890'
    address = 'Avenue XX Street YY'
    city = 'Cali'
    birth_date = '2024-01-01'
    is_active = True
    is_staff = False
    is_superuser = False

    if not User.objects.filter(email=email).exists():
        user = User.objects.create(
            email=email, user_id=user_id, first_name=first_name, last_name=last_name,
            second_last_name=second_last_name, contact_number=contact_number,
            address=address, city=city, birth_date=birth_date, is_active=is_active,
            is_staff=is_staff, is_superuser=is_superuser
        )
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
    

def test_user_second_last_name(test_user):
    assert test_user.get_second_last_name() == 'Prueba'
    
    
def test_user_contact_number(test_user):
    assert test_user.get_contact_number() == '1234567890'
    
    
def test_user_address(test_user):
    assert test_user.get_address() == 'Avenue XX Street YY'


def test_user_city(test_user):
    assert test_user.get_city() == 'Cali'


def test_user_birth_date(test_user):
    assert test_user.get_birth_date() == datetime.date(2024, 1, 1)


def test_user_is_active(test_user):
    assert test_user.get_is_active()


def test_user_is_staff(test_user):
    assert not test_user.get_is_staff()


def test_user_is_superuser(test_user):
    assert not test_user.get_is_superuser() 