from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        if user.is_superuser:
            token['user_type'] = 'superuser'

        elif user.is_staff:
            token['user_type'] = 'staff'

        else:
            token['user_type'] = 'student'

        return token
