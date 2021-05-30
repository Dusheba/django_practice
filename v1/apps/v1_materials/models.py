from django.db import models
from v1.apps.v1_tasks.models import Task
from v1.apps.v1_lessons.models import Lesson


class Material(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )
    text = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    video_url = models.URLField(
        max_length=200,
        null=True,
        blank=True
    )
    file = models.FileField(
        verbose_name="file of material",
        upload_to='files/',
        null=True,
        blank=True
    )
    photo = models.FileField(
        verbose_name="photo of material",
        upload_to='photos/',
        null=True,
        blank=True
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.text,
        self.video_url,
        self.photo,
        self.lesson,
        self.file,
        self.description,
    )
