from django.test import TestCase
from django.urls import reverse

from ..factories import QuestionFactory, ChoiceFactory


class QuestionListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('polls:index')

    def test_al_crear_una_encuesta_debe_aparecer_en_el_listado(self):
        QuestionFactory.create(
            text='COVID-19 una amenaza para la humanidad'
        )

        response = self.client.get(self.url)

        self.assertContains(response, 'COVID-19 una amenaza para la humanidad')

    def test_si_una_encuesta_esta_cerrada_no_debe_aparecer_en_el_listado(self):
        QuestionFactory.create(
            text='No debe aparecer',
            open=False
        )

        response = self.client.get(self.url)

        self.assertNotContains(response, 'No debe aparecer')

    def test_cuando_no_hay_encuetas_abiertas_debe_aparecer_un_mensaje(self):

        response = self.client.get(self.url)

        self.assertContains(response, 'No hay encuestas abiertas.')


class QuestionDetailView(TestCase):

    def test_puedo_ver_las_opciones_de_una_encuesta(self):

        poll = QuestionFactory.create(text='Mi encuesta')

        ChoiceFactory.create(text='Uno', poll=poll)
        ChoiceFactory.create(text='Dos', poll=poll)

        url = reverse('polls:detail', kwargs={'pk': poll.pk})

        response = self.client.get(url)

        self.assertContains(response, 'Uno')
        self.assertContains(response, 'Dos')
        self.assertEqual(2, len(response.context['choices']))
