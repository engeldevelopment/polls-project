from django.db import models


class QuestionQuerySet(models.QuerySet):

    def open(self):
        return self.filter(open=True)
