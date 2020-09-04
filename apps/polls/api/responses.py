from rest_framework import response
from rest_framework import status


class QuestionIsClosed(response.Response):

    def __init__(
            self,
            data={'detail': 'Esta encuesta está cerrada.'},
            status=status.HTTP_204_NO_CONTENT,
            template_name=None,
            headers=None,
            exception=False,
            content_type=None):
        super().__init__(
            data,
            status,
            template_name,
            headers,
            exception,
            content_type
        )


class QuestionWithoutResults(response.Response):
    def __init__(
            self,
            data={
                "detail": "De esta encuesta no hay resultados que mostrar."
            },
            status=status.HTTP_204_NO_CONTENT,
            template_name=None,
            headers=None,
            exception=False,
            content_type=None):
        super().__init__(
            data,
            status,
            template_name,
            headers,
            exception,
            content_type
        )
