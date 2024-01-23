from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import (MAX_EMAIL_CHARACTERS,
                        MAX_NAME_PASSWORD_CHARACTERS)
from .validators import validator_username


class User(AbstractUser):
    """ Класс пользователей. """
    username = models.CharField(
        'Логин',
        max_length=MAX_NAME_PASSWORD_CHARACTERS,
        unique=True,
        help_text=('Не более 20 символов. '
                   'Только буквы и цифры, символы @+-'),
        validators=(validator_username,),
        error_messages={
            'unique': 'Пользователь с таким именем уже есть',
        }
    )
    email = models.EmailField('E-mail', max_length=MAX_EMAIL_CHARACTERS,
                              unique=True)
    first_name = models.CharField('Имя',
                                  max_length=MAX_NAME_PASSWORD_CHARACTERS)
    last_name = models.CharField('Фамилия',
                                 max_length=MAX_NAME_PASSWORD_CHARACTERS)
    password = models.CharField('Пароль',
                                max_length=MAX_NAME_PASSWORD_CHARACTERS)
    is_in_black_list = models.BooleanField('В черном списке',
                                           default=False)

    class Meta:
        ordering = ('username',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
