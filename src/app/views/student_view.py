from rest_framework import viewsets
# from rest_framework.response import Response
from ..serializers.student_serializer import StudentSerializer
from ..models.student_model import Student


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
