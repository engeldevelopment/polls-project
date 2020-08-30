from django.db import models
from django.urls import reverse

from .managers import QuestionManager


class Question(models.Model):
    text = models.CharField(max_length=100)
    open = models.BooleanField(default=True)

    objects = QuestionManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})

    def get_absolute_results_url(self):
        return reverse('polls:results', kwargs={'pk': self.pk})


class Choice(models.Model):
    text = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)
    poll = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )

    def __str__(self):
        return self.text

    def vote(self):
        self.votes += 1
        self.save()
