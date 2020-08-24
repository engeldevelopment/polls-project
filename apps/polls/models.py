from django.db import models

from .managers import PollManager


class Poll(models.Model):
    text = models.CharField(max_length=100)
    open = models.BooleanField(default=True)

    objects = PollManager()

    def __str__(self):
        return self.text
