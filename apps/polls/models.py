from django.db import models


class Poll(models.Model):
    text = models.CharField(max_length=100)
    open = models.BooleanField(default=True)

    def __str__(self):
        return self.text
