from .tests_in_common import *
import datetime




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