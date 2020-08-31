from rest_framework import generics

from .serializers import QuestionSerializer
from ..models import Question


class QuestionResultAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.open()
