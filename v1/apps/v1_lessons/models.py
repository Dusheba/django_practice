from django.db import models

from v1.apps.v1_courses.models import Course


class Lesson(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        verbose_name="date of creation",
        editable=False
    )
    materials_num = models.IntegerField(
        verbose_name="number of materials",
        blank=True,
        null=True
    )
    last_update = models.DateTimeField(
        verbose_name="last update",
        blank=True,
        null=True,

        )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.description,
        self.course,
        self.date_created,
        self.materials_num,
        self.last_update,
    )
