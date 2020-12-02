from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')

        user = self.model(username=username,
                             email=self.normalize_email(email),
                             first_name=first_name,
                             last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(email,
                                   username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user



class Usuario(AbstractBaseUser):
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=100,primary_key=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    first_name = models.CharField('first_name', max_length=70, null=False)
    last_name = models.CharField('last_name', max_length=70, null=False)
    picture = models.ImageField(
        'picture', upload_to='perfil/', max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True