from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, user_id, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email válido')
        email = self.normalize_email(email)

        if not user_id:
            raise ValueError('El usuario debe tener un id válido')

        user = self.model(email=email, user_id=user_id,
                          first_name=first_name, last_name=last_name, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, user_id, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_superuser') is True:
            raise ValueError(
                'Un usuario normal no puede tener el parámetro is_superuser = True')

        return self._create_user(email, user_id, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, user_id, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'El superusuario debe tener el parámetro is_staff = True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'El superusuario debe tener el parámetro is_superuser = True')

        return self._create_user(email, user_id, first_name, last_name, password, **extra_fields)
