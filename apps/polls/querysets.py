from django.db import models


class PollQuerySet(models.QuerySet):

    def open(self):
        return self.filter(open=True)
