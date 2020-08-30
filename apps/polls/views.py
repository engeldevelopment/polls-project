from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .mixins import QuestionDetailViewMixin
from .models import Question, Choice


class QuestionListView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Question.objects.open()


class QuestionDetailView(
        QuestionDetailViewMixin,
        generic.DeleteView):

    template_name = 'polls/detail.html'


class QuestionVoteView(generic.View):

    def post(self, request):
        question = get_object_or_404(Question, pk=request.POST['question'])

        try:
            choice = question.choices.get(pk=request.POST['choice'])
            choice.vote()
        except(KeyError, Choice.DoesNotExist):
            context = {
                'question': question,
                'message': 'Debes elegir una opción por favor...',
                'choices': question.choices.all()
            }
            return render(request, 'polls/detail.html', context)
        return redirect(question.get_absolute_results_url())


class QuestionResultView(
        QuestionDetailViewMixin,
        generic.DetailView):

    template_name = 'polls/results.html'
