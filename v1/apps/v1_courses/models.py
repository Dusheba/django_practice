from django.db import models
from v1.apps.v1_users.models import User
from v1.apps.v1_themes.models import Theme


class Course(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=300
    )
    theme = models.ManyToManyField(
        Theme,
        related_name="theme"
    )
    curator = models.ManyToManyField(
        User,
        related_name="course_curator"
    )
    listener = models.ManyToManyField(
        User,
        related_name="listener"
    )
    rating = models.FloatField(
        verbose_name="course rating",
        default=0
    )
    date_created = models.DateField(
        verbose_name="date of creation",
        editable=False
        )
    lesson_num = models.IntegerField(
        verbose_name="number of lessons",
        default=0
    )
    last_update = models.DateTimeField(
        verbose_name="last update",
        blank=True,
        null=True
        )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.description,
        self.theme,
        self.listener,
        self.rating,
        self.curator,
        self.rating,
        self.date_created,
        self.lesson_num,
        self.last_update,
    )
