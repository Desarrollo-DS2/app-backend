from django.db import models
from .user_model import User


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    role = models.CharField('Rol', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'Empleado: {str(self.user)}'

    def get_role(self):
        return self.role
