from django.urls import resolve

from rest_framework.test import APISimpleTestCase

from ...api import views


class QuestionEndPointAPI(APISimpleTestCase):

    def test_obtener_los_resultados_de_una_encuesta(self):

        url = '/api/v1/question/1/results'

        self.assertEqual(
            views.QuestionResultAPIView,
            resolve(url).func.view_class
        )
