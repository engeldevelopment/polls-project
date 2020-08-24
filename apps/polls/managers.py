from django.db import models

from .querysets import PollQuerySet


class PollManager(models.Manager):

    def get_queryset(self):
        return PollQuerySet(self.model, using=self._db)

    def open(self):
        return self.get_queryset().open()
