from django.db import models
from django.urls import reverse

from .managers import PollManager


class Poll(models.Model):
    text = models.CharField(max_length=100)
    open = models.BooleanField(default=True)

    objects = PollManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})


class Choice(models.Model):
    text = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='choices'
    )

    def __str__(self):
        return self.text
