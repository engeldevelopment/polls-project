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


class QuestionVoteView(TestCase):

    def setUp(self):

        self.question = QuestionFactory.create(
            text='Las mujeres son problemáticas'
        )

        self.opcion_si = ChoiceFactory.create(
            text='Sí',
            poll=self.question
        )
        ChoiceFactory.create(
            text='No',
            poll=self.question
        )

        self.url = reverse('polls:vote')

    def test_cuando_no_elijo_una_opcion_da_error(self):
        data = {
            'choice': 0,
            'question': self.question.pk
        }

        response = self.client.post(self.url, data)

        self.assertContains(response, 'Debes elegir una opción por favor...')

    def test_cuando_elijo_una_opcion_deberia_mostrar_los_resultados(self):
        data = {
            'choice': self.opcion_si.pk,
            'question': self.question.pk
        }

        response = self.client.post(self.url, data)

        self.assertRedirects(
            response,
            reverse('polls:results', kwargs={'pk': self.question.pk})
        )


class QuestionResultViewTest(TestCase):

    def test_no_se_mostraran_resultados_de_una_encuesta_cerrada(self):
        question = QuestionFactory.create(
            text='Test',
            open=False
        )
        url = reverse('polls:results', kwargs={'pk': question.pk})

        response = self.client.get(url)

        self.assertContains(
            response,
            'Esta encuesta está cerrada.'
        )

    def test_no_se_mostraran_resultados_de_una_encuesta_sin_opciones(self):
        question = QuestionFactory.create(
            text='Test',
            open=True
        )
        url = reverse('polls:results', kwargs={'pk': question.pk})

        response = self.client.get(url)

        self.assertContains(
            response,
            'De esta encuesta no hay resultados que mostrar.'
        )
