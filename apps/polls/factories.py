from factory.django import DjangoModelFactory

from .models import Poll


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll

    text = 'Mi encuesta'
    open = True
