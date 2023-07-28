import random

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    word_list = list("Password12345")
    ver_code = "".join(random.sample(word_list, len(word_list)))

    username = None

    email = models.EmailField(verbose_name='Email', unique=True)

    verification_code = models.CharField(max_length=35, verbose_name='код верификации', default=ver_code)
    is_active = models.BooleanField(default=False, verbose_name='активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
