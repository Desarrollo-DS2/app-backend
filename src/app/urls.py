from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views.user_view import UserViewSet
from .views.student_view import StudentViewSet
from .views.employee_view import EmployeeViewSet
from .views.recaptcha_view import RecaptchaView


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, 'user')
router.register(r'students', StudentViewSet, 'student')
router.register(r'employees', EmployeeViewSet, 'employee')

urlpatterns = [
    path('docs/', include_docs_urls(title='main app API documentation')),
    path('api/', include(router.urls)),
    path('api/recaptcha/', RecaptchaView, name='recaptcha'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]
