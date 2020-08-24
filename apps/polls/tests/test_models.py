from django.test import TestCase

from ..factories import PollFactory
from ..models import Poll


class PollTest(TestCase):

    def test_no_hay_encuestas_abiertas(self):

        self.assertEqual(0, Poll.objects.open().count())

    def test_cuendo_hay_encuestas_abiertas_deben_aparecer(self):

        PollFactory.create(open=True)

        self.assertEqual(1, Poll.objects.open().count())
