from .user_serializer import UserSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction
from ..models.user_model import User
from ..models.employee_model import Employee


class EmployeeSerializer(UserSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    user_id = serializers.CharField(source='user.user_id')

    first_name = serializers.CharField(
        source='user.first_name', read_only=True)

    middle_name = serializers.CharField(
        source='user.middle_name', read_only=True)

    last_name = serializers.CharField(source='user.last_name', read_only=True)

    second_last_name = serializers.CharField(
        source='user.second_last_name', read_only=True)

    contact_number = serializers.CharField(
        source='user.contact_number', read_only=True)

    address = serializers.CharField(
        source='user.address', read_only=True)

    city = serializers.CharField(
        source='user.city', read_only=True)

    birth_date = serializers.DateField(
        source='user.birth_date', read_only=True)

    is_staff = serializers.BooleanField(source='user.is_staff', read_only=True)

    is_superuser = serializers.BooleanField(
        source='user.is_superuser', read_only=True)

    password = serializers.CharField(
        source='user.password', allow_blank=True, allow_null=True, write_only=True, required=False)

    class Meta(UserSerializer.Meta):
        model = Employee
        fields = UserSerializer.Meta.fields + ['role']

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')

        try:
            user = User.objects.get(user_id=user_data['user_id'])

            employee = Employee.objects.create(user=user, **validated_data)
            return employee

        except Exception as exception:
            raise ValidationError({type(exception).__name__: str(exception)})
