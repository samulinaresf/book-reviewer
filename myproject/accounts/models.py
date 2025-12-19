from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class ManagerAccount(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("El email es un campo requerido.")
        if not username:
            raise ValueError("El usuario es un campo requerido.")
        if not first_name:
            raise ValueError("El nombre es un campo requerido.")

        # Crear el usuario correctamente, sin pasar 'self'
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, password=None):
        # Usar 'create_user' para inicializar al superusuario
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name='',  # Opcional para el superusuario
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    date_birth = models.DateField(blank=True, null=True)
    
    # Campos de membresía y administración
    is_member = models.BooleanField(default=False)
    membership_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Campo de autenticación principal
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    # Administrador de cuentas personalizado
    objects = ManagerAccount()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
