from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, telefono, nombre, apellido_paterno, apellido_materno, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, telefono=telefono, nombre=nombre,
                          apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, telefono, nombre, apellido_paterno, apellido_materno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, telefono, nombre, apellido_paterno, apellido_materno, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['telefono', 'nombre', 'apellido_paterno', 'apellido_materno']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    def get_short_name(self):
        return self.nombre