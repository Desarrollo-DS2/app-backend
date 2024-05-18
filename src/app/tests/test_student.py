import pytest
from ..models.student_model import Student
from django.contrib.auth import get_user_model

User = get_user_model()

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


def test_student_is_student_worker(test_student):
    assert not test_student.get_is_student_worker()


def test_student_number_of_tickets(test_student):
    assert test_student.get_number_of_tickets() == 5
