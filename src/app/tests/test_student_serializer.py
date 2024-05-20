import pytest
from django.contrib.auth import get_user_model
from ..serializers.student_serializer import StudentSerializer
from ..models.student_model import Student

User = get_user_model()

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
def test_student(db, test_user):
    is_student_worker = True
    number_of_tickets = 5

    if not Student.objects.filter(user=test_user).exists():
        student = Student.objects.create(
            user=test_user, is_student_worker=is_student_worker, number_of_tickets=number_of_tickets)
        student.save()

    yield Student.objects.get(user=test_user)

    Student.objects.get(user=test_user).delete()

def test_student_serializer(test_student):
    serializer = StudentSerializer(test_student)
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