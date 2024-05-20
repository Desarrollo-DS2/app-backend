import pytest
from ..serializers.token_serializer import TokenPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def create_user():
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def create_superuser():
    def make_superuser(**kwargs):
        return User.objects.create_superuser(**kwargs)
    return make_superuser

@pytest.fixture
def superuser(create_superuser):
    return create_superuser(
        email='superuser@example.com',
        user_id='45454545',
        first_name='Super',
        last_name='User',
        password='password123',
        is_superuser=True
    )

@pytest.fixture
def staff_user(create_user):
    return create_user(
        email='staff@example.com',
        user_id='12345678',
        first_name='Staff',
        last_name='User',
        password='password123',
        is_staff=True
    )

@pytest.fixture
def student_user(create_user):
    return create_user(
        email='student@example.com',
        user_id='98513204',
        first_name='Student',
        last_name='User',
        password='password123'
    )

def test_superuser_token(superuser):
    serializer = TokenPairSerializer()
    token = serializer.get_token(superuser)

    assert token['email'] == superuser.email
    assert token['first_name'] == superuser.first_name
    assert token['last_name'] == superuser.last_name
    assert token['user_type'] == 'superuser'

def test_staff_user_token(staff_user):
    serializer = TokenPairSerializer()
    token = serializer.get_token(staff_user)

    assert token['email'] == staff_user.email
    assert token['first_name'] == staff_user.first_name
    assert token['last_name'] == staff_user.last_name
    assert token['user_type'] == 'staff'

def test_student_user_token(student_user):
    serializer = TokenPairSerializer()
    token = serializer.get_token(student_user)

    assert token['email'] == student_user.email
    assert token['first_name'] == student_user.first_name
    assert token['last_name'] == student_user.last_name
    assert token['user_type'] == 'student'