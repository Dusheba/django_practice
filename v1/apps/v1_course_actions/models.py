from django.db import models

from v1.apps.v1_courses.models import Course
from v1.apps.v1_users.models import User


class CourseAction(models.Model):
    listener = models.ManyToManyField(
        User,
        related_name="course_action_listener"
    )
    course = models.ManyToManyField(
        Course,
        related_name="course_action"
    )
    is_selected = models.BooleanField(
        default=False
    )
    is_completed = models.BooleanField(
        default=False
    )
    is_uncompleted = models.BooleanField(
        default=False
    )


def __str__(self):
    return "{} {}".format(
        self.listener,
        self.course,
        self.id_selected,
        self.is_completed,
        self.is_uncompleted,
    )
