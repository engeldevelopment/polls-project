from django.test import TestCase
from django.urls import reverse

from ..factories import PollFactory


class PollListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('polls:index')

    def test_al_crear_una_encuesta_debe_aparecer_en_el_listado(self):
        PollFactory.create(
            text='COVID-19 una amenaza para la humanidad'
        )

        response = self.client.get(self.url)

        self.assertContains(response, 'COVID-19 una amenaza para la humanidad')

    def test_si_una_encuesta_esta_cerrada_no_debe_aparecer_en_el_listado(self):
        PollFactory.create(
            text='No debe aparecer',
            open=False
        )

        response = self.client.get(self.url)

        self.assertNotContains(response, 'No debe aparecer')

    def test_cuando_no_hay_encuetas_abiertas_debe_aparecer_un_mensaje(self):

        response = self.client.get(self.url)

        self.assertContains(response, 'No hay encuestas abiertas.')
