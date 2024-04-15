from django.db import models
from .user_model import User


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    is_student_worker = models.BooleanField(
        'Es monitor estudiantil', default=False)

    number_of_tickets = models.PositiveIntegerField(
        'Número de Tiquetes', blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f'Estudiante: {str(self.user)}'

    def get_is_student_worker(self):
        return self.is_student_worker

    def get_number_of_tickets(self):
        return self.number_of_tickets
