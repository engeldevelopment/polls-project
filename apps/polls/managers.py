from django.db import models

from .querysets import QuestionQuerySet


class QuestionManager(models.Manager):

    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)

    def open(self):
        return self.get_queryset().open()
