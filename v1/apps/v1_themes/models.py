from django.db import models


class Theme(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=300
    )


def __str__(self):
    return "{} {}".format(
        self.name,
        self.description,
    )
