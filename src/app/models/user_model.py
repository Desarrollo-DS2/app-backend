from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electrónico', unique=True)

    user_id = models.CharField(
        'Número de Identificación', max_length=15, primary_key=True, unique=True)

    first_name = models.CharField('Primer Nombre', max_length=30)

    middle_name = models.CharField(
        'Segundo Nombre', max_length=30, blank=True, null=True)

    last_name = models.CharField('Primer Apellido', max_length=30)

    second_last_name = models.CharField(
        'Segundo Apellido', max_length=30, blank=True, null=True)

    contact_number = models.CharField(
        'Teléfono de Contacto', max_length=15, blank=True, null=True)

    address = models.CharField(
        'Dirección', max_length=100, blank=True, null=True)

    city = models.CharField('Ciudad', max_length=30, blank=True, null=True)

    birth_date = models.DateField('Fecha de Nacimiento', blank=True, null=True)

    is_active = models.BooleanField('Usuario Activo', default=True)

    is_staff = models.BooleanField('Usuario parte del Staff', default=False)

    is_superuser = models.BooleanField('Superusuario', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{str(self.user_id)} - {self.email} - {self.first_name} {self.last_name}'

    def get_email(self):
        return self.email

    def get_user_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_second_last_name(self):
        return self.second_last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_contact_number(self):
        return self.contact_number

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_birth_date(self):
        return self.birth_date

    def get_is_active(self):
        return self.is_active

    def get_is_staff(self):
        return self.is_staff

    def get_is_superuser(self):
        return self.is_superuser
