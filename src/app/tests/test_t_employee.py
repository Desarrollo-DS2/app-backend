import pytest
from ..models.employee_model import Employee
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def test_employee(db):
    email = 'empleado@gmail.com'
    user_id = '20202020'
    first_name = 'Empleado'
    last_name = 'Prueba'
    password = 'password123'    
    role = 'Gerente'

    if not User.objects.filter(email=email).exists():
        user = User.objects.create(
            email=email, user_id=user_id, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

    if not Employee.objects.filter(user=user).exists():
        employee = Employee.objects.create(
            user=user, role=role)
        employee.save()

    yield Employee.objects.get(user=user)

    Employee.objects.get(user=user).delete()

def test_employee_role(test_employee):
    assert test_employee.get_role() == 'Gerente'