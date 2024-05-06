from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction
from ..models.user_model import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'user_id', 'first_name', 'middle_name', 'last_name', 'second_last_name',
                  'contact_number', 'address', 'city', 'birth_date', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres')

        if not re.search('[A-Z]', value):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula')

        if not re.search('[a-z]', value):
            raise ValidationError('La contraseña debe tener al menos una letra minúscula')

        if not re.search('[0-9]', value):
            raise ValidationError('La contraseña debe tener al menos un número')

        if not re.search('[@_!#$%&*]', value):
            raise ValidationError(
                'La contraseña debe tener al menos uno de los siguientes caracteres especiales: @_!#$%&*')

        return value

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password', None)

        try:
            user = User.objects.create(**validated_data)
            if password is not None:
                user.set_password(password)

            user.save()
            return user

        except Exception as exception:
            raise ValidationError({type(exception).__name__: str(exception)})
