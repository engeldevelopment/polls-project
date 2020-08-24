from factory.django import DjangoModelFactory
from factory import SubFactory

from .models import Poll, Choice


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll

    text = 'Mi encuesta'
    open = True


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    text = 'Opcion'
    poll = SubFactory(PollFactory)
