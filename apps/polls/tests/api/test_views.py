from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from ...factories import ChoiceFactory, QuestionFactory


class QuestionAPIView(APITestCase):

    def test_cuando_busco_una_encuesta_deberia_retornar_sus_resultados(self):
        question = QuestionFactory.create(
            text="¿El dinero es más importante que la vida?"
        )

        ChoiceFactory.create(
            text='Sí',
            poll=question,
            votes=20
        )
        ChoiceFactory.create(
            text='No',
            poll=question,
            votes=11
        )
        url = reverse('polls:results_api', kwargs={'pk': question.pk})

        response = self.client.get(url)

        response_data = {
            'id': question.pk,
            'text': question.text,
            'choices': [
                {
                    'text': 'Sí',
                    'votes': 20
                },
                {
                    'text': 'No',
                    'votes': 11
                }
            ]
        }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response_data, response.data)

    def test_retorna_un_404_cuando_una_encuesta_no_existe(self):

        url = reverse('polls:results_api', kwargs={'pk': 100})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_no_se_daran_resultados_de_una_encuesta_cerrada(self):
        question = QuestionFactory.create(
            text="Está cerrada",
            open=False
        )
        url = reverse('polls:results_api', kwargs={'pk': question.pk})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_no_se_daran_resultados_de_una_encuesta_sin_opciones(self):
        question = QuestionFactory.create(
            text="Está cerrada",
            open=True
        )
        url = reverse('polls:results_api', kwargs={'pk': question.pk})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
