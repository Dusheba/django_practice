from django.db import models

from v1.apps.v1_lessons.models import Lesson


class Task(models.Model):
    name = models.CharField(
        max_length=100
    )
    max_points = models.IntegerField(
        verbose_name="maximum points",
    )
    min_points = models.IntegerField(
        verbose_name="minimum points for passing",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.max_points,
        self.min_points,
        self.lesson
    )
