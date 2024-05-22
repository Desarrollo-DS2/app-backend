import pytest
from ..models.user_model import User
from ..models.student_model import Student
from ..models.employee_model import Employee

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
    
@pytest.fixture
def test_student(db):
    email = 'prueba@gmail.com'
    user_id = '10101010'
    first_name = 'Prueba'
    last_name = 'Prueba'
    password = 'password123'    
    is_student_worker = False
    number_of_tickets = 5

    if not User.objects.filter(email=email).exists():
        user = User.objects.create(
            email=email, user_id=user_id, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

    if not Student.objects.filter(user=user).exists():
        student = Student.objects.create(
            user=user, is_student_worker=is_student_worker, number_of_tickets=number_of_tickets)
        student.save()

    yield Student.objects.get(user=user)

    Student.objects.get(user=user).delete()    
    
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