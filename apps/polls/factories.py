from factory.django import DjangoModelFactory
from factory import SubFactory

from .models import Question, Choice


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    text = 'Mi encuesta'
    open = True


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    text = 'Opcion'
    poll = SubFactory(QuestionFactory)
