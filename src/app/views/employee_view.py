from rest_framework import viewsets
# from rest_framework.response import Response
from ..serializers.employee_serializer import EmployeeSerializer
from ..models.employee_model import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
