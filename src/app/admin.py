from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_superuser']
    search_fields = ['user_id', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser']
    list_per_page = 10


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'number_of_tickets']
    list_per_page = 10


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'role']
    list_per_page = 10
