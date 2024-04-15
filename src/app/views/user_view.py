from rest_framework import viewsets
# from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer
from ..models.user_model import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
