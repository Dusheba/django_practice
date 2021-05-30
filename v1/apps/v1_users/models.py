from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=30,
        blank=True
    )
    patronymic = models.CharField(
        verbose_name='last name',
        max_length=30,
        blank=True
    )
    birth_date = models.DateField(
        verbose_name="date of birth"
    )
    social_networks = models.URLField(
        max_length=200
    )
    photo = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )
    last_login = models.DateTimeField(
        verbose_name="last login",
        blank=True,
        null=True
    )
    admin = models.BooleanField(
        default=False
    )
    curator = models.BooleanField(
        default=False
    )


def __str__(self):
    return "{} {}".format(
        self.last_name,
        self.first_name,
        self.patronymic,
        self.email,
        self.photo,
        self.birth_date,
        self.cosial_networks,
        self.photo,
        self.admin,
        self.curator,
        self.last_login
    )
