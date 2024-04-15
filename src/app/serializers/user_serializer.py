from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction
from ..models.user_model import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'user_id', 'first_name', 'middle_name', 'last_name', 'second_last_name',
                  'contact_number', 'address', 'city', 'birth_date', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {'password': {'write_only': True}}

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
