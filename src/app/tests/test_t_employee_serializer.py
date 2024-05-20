import pytest
from django.contrib.auth import get_user_model
from ..serializers.employee_serializer import EmployeeSerializer
from ..models.employee_model import Employee
from .tests_in_common import *

User = get_user_model()


@pytest.fixture
def test_employee(db, test_user):
    role = 'Empleado'

    if not Employee.objects.filter(user=test_user).exists():
        employee = Employee.objects.create(
            user=test_user, role=role)
        employee.save()

    yield Employee.objects.get(user=test_user)

    Employee.objects.get(user=test_user).delete()

def test_employee_serializer(test_employee):
    serializer = EmployeeSerializer(test_employee)
    data = serializer.data

    assert data['email'] == 'prueba@gmail.com'
    assert data['user_id'] == '10101010'
    assert data['first_name'] == 'Prueba'
    assert data['last_name'] == 'Prueba'                
    assert data['role'] == 'Empleado'
    assert data['second_last_name'] == 'Prueba'
    assert data['contact_number'] == '1234567890'
    assert data['address'] == 'Avenue XX Street YY'
    assert data['city'] == 'Cali'
    assert data['birth_date'] == '2024-01-01'
    assert not data['is_staff']
    assert not data['is_superuser']
    assert 'password' not in data  # La contraseña no debe estar en la data serializada    