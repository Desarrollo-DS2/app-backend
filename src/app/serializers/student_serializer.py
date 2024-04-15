from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction
from .user_serializer import UserSerializer
from ..models.student_model import Student


class StudentSerializer(UserSerializer):
    email = serializers.EmailField(source='user.email')

    user_id = serializers.CharField(source='user.user_id')

    first_name = serializers.CharField(source='user.first_name')

    middle_name = serializers.CharField(
        source='user.middle_name', allow_blank=True, allow_null=True)

    last_name = serializers.CharField(source='user.last_name')

    second_last_name = serializers.CharField(
        source='user.second_last_name', allow_blank=True, allow_null=True)

    contact_number = serializers.CharField(
        source='user.contact_number', allow_blank=True, allow_null=True)

    address = serializers.CharField(
        source='user.address', allow_blank=True, allow_null=True)

    city = serializers.CharField(
        source='user.city', allow_blank=True, allow_null=True)

    birth_date = serializers.DateField(
        source='user.birth_date', allow_null=True)

    is_staff = serializers.BooleanField(source='user.is_staff')

    is_superuser = serializers.BooleanField(source='user.is_superuser')

    password = serializers.CharField(source='user.password', write_only=True)

    class Meta(UserSerializer.Meta):
        model = Student
        fields = UserSerializer.Meta.fields + \
            ['is_student_worker', 'number_of_tickets']

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')

        try:
            user = super().create(user_data)
            student = Student.objects.create(user=user, **validated_data)
            return student

        except Exception as exception:
            raise ValidationError({type(exception).__name__: str(exception)})
