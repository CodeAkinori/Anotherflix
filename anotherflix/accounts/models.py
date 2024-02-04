from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # O campo 'username' e 'password' já são fornecidos pelo AbstractUser
    # Se precisar de mais campos, adicione-os aqui
    # Exemplo: Adicionando um campo para o nome completo
    full_name = models.CharField(max_length=100, blank=True)

    # Modificar os campos 'groups' e 'user_permissions' para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
