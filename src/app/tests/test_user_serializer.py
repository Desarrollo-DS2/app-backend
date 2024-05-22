import pytest
from django.contrib.auth import get_user_model
from ..serializers.user_serializer import UserSerializer
from .tests_in_common import *

User = get_user_model()

def test_user_serializer(test_user):
    serializer = UserSerializer(test_user)
    data = serializer.data

    assert data['email'] == 'prueba@gmail.com'
    assert data['user_id'] == '10101010'
    assert data['first_name'] == 'Prueba'
    assert data['last_name'] == 'Prueba'
    assert data['second_last_name'] == 'Prueba'
    assert data['contact_number'] == '1234567890'
    assert data['address'] == 'Avenue XX Street YY'
    assert data['city'] == 'Cali'
    assert data['birth_date'] == '2024-01-01'
    assert not data['is_staff']
    assert not data['is_superuser']
    assert 'password' not in data  # La contraseña no debe estar en la data serializada
    
def test_password_validation(db):
    test_user_data = {
        'email': 'prueba@gmail.com',
        'user_id': '10101010',
        'first_name': 'Prueba',
        'last_name': 'Prueba',
        'second_last_name': 'Prueba',
        'contact_number': '1234567890',
        'address': 'Avenue XX Street YY',
        'city': 'Cali',
        'birth_date': '2024-01-01',
        'is_staff': False,
        'is_superuser': False,
        'password': 'Password123@'
    }
        
    # Prueba de contraseña demasiado corta
    test_user_data['password'] = 'Pass1@'
    serializer = UserSerializer(data=test_user_data)
    assert not serializer.is_valid()
    assert 'La contraseña debe tener al menos 8 caracteres' in serializer.errors['password']    
    
    # Prueba de contraseña sin letra mayúscula
    test_user_data['password'] = 'password1@'
    serializer = UserSerializer(data=test_user_data)
    assert not serializer.is_valid()
    assert 'La contraseña debe tener al menos una letra mayúscula' in serializer.errors['password']  
    
    # Prueba de contraseña sin letra minúscula
    test_user_data['password'] = 'PASSWORD1@'
    serializer = UserSerializer(data=test_user_data)
    assert not serializer.is_valid()
    assert 'La contraseña debe tener al menos una letra minúscula' in serializer.errors['password']     
    
    # Prueba de contraseña sin número
    test_user_data['password'] = 'Password@'
    serializer = UserSerializer(data=test_user_data)
    assert not serializer.is_valid()
    assert 'La contraseña debe tener al menos un número' in serializer.errors['password']
    
    # Prueba de contraseña sin carácter especial
    test_user_data['password'] = 'Password1'
    serializer = UserSerializer(data=test_user_data)    
    assert not serializer.is_valid()
    assert 'La contraseña debe tener al menos uno de los siguientes caracteres especiales: @_!#$%&*' in serializer.errors['password']       

def test_user_creation(db):
    test_user_data = {
        'email': 'prueba@gmail.com',
        'user_id': '10101010',
        'first_name': 'Prueba',
        'last_name': 'Prueba',
        'second_last_name': 'Prueba',
        'contact_number': '1234567890',
        'address': 'Avenue XX Street YY',
        'city': 'Cali',
        'birth_date': '2024-01-01',
        'is_staff': False,
        'is_superuser': False,
        'password': 'Password123@'
    }

    serializer = UserSerializer(data=test_user_data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == test_user_data['email']
    assert user.check_password(test_user_data['password'])
    
def test_user_creation_with_existing_email(db, test_user):
    test_user_data = {
        'email': test_user.email,  # Usar el mismo correo electrónico que el usuario de prueba existente
        'user_id': '20202020',
        'first_name': 'Prueba2',
        'last_name': 'Prueba2',
        'second_last_name': 'Prueba2',
        'contact_number': '0987654321',
        'address': 'Avenue ZZ Street XX',
        'city': 'Bogota',
        'birth_date': '2024-02-02',
        'is_staff': True,
        'is_superuser': True,
        'password': 'Password456@'
    }

    serializer = UserSerializer(data=test_user_data)
    assert not serializer.is_valid()
    assert 'Ya existe un/a Usuario con este/a Correo Electrónico.' in serializer.errors['email']    