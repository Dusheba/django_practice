from django.db import models
from v1.apps.v1_lessons.models import Lesson
from v1.apps.v1_materials.models import Material
from v1.apps.v1_tasks.models import Task
from v1.apps.v1_users.models import User


class LessonAction(models.Model):
    listener = models.ManyToManyField(
        User,
        related_name="lesson_action_user"
    )
    user_points = models.IntegerField(
        verbose_name="user_points",
    )
    mark = models.IntegerField(
        verbose_name="user_mark",
    )
    material = models.ManyToManyField(
        Material,
        related_name="material_action",
        blank=True,
    )
    material_completed = models.BooleanField(
        default=False,
        blank=True,
        null=True
    )
    task = models.ManyToManyField(
        Task,
        related_name="task_action",
        blank=True,
    )
    last_task = models.ManyToManyField(
        Task,
        related_name="last_task",
        blank=True,
    )
    task_completed = models.BooleanField(
        default=False,
        blank=True,
        null=True
    )
    lesson = models.ManyToManyField(
        Lesson,
        related_name="lesson_action",
        blank=True,
    )
    last_lesson = models.ManyToManyField(
        Task,
        related_name="last_lesson",
        blank=True,
    )
    lesson_completed = models.BooleanField(
        default=False,
        blank=True,
        null=True
    )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.user_points,
        self.mark,
        self.material,
        self.material_completed,
        self.task,
        self.last_task,
        self.task_completed,
        self.lesson,
        self.last_lesson,
        self.lesson_completed,
    )
