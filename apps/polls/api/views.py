from rest_framework import generics

from .responses import QuestionIsClosed, QuestionWithoutResults
from .serializers import QuestionSerializer
from ..models import Question


class QuestionResultAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def retrieve(self, request, *args, **kwargs):
        question = self.get_object()
        if not question.open:
            return QuestionIsClosed()
        if not question.has_choices():
            return QuestionWithoutResults()
        return super().retrieve(request, *args, **kwargs)
