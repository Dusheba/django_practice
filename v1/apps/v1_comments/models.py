from django.db import models
from v1.apps.v1_lessons.models import Lesson
from v1.apps.v1_users.models import User


class Comment(models.Model):
    listener = models.ManyToManyField(
        User,
        related_name="listener_comment"
    )
    lesson = models.ManyToManyField(
        Lesson,
        related_name="comment_to_lesson"
    )
    text = models.CharField(
        verbose_name="text of comment",
        max_length=500
    )
    date = models.DateTimeField(
        verbose_name="date of adding",
    )


def __str__(self):
    return "{} {}".format(
        self.listener,
        self.lesson,
        self.date
    )
