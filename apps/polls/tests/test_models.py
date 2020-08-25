from django.test import TestCase

from ..factories import QuestionFactory, ChoiceFactory
from ..models import Question


class QuestionTest(TestCase):

    def test_no_hay_encuestas_abiertas(self):

        self.assertEqual(0, Question.objects.open().count())

    def test_cuendo_hay_encuestas_abiertas_deben_aparecer(self):

        QuestionFactory.create(open=True)

        self.assertEqual(1, Question.objects.open().count())

    def test_puedo_agregar_opciones_a_una_encuesta(self):

        poll = QuestionFactory.create(text="¿Las caraotas llevan azúcar?")

        ChoiceFactory.create(text="si", poll=poll)
        ChoiceFactory.create(text="no", poll=poll)

        self.assertEqual(2, poll.choices.count())
