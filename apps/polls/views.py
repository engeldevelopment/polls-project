from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class QuestionListView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Question.objects.open()


class QuestionDetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.get_object().choices.all()
        context['choices'] = choices
        return context


class QuestionVoteView(generic.View):

    def post(self, request):
        question = get_object_or_404(Question, pk=request.POST['question'])

        try:
            choice = question.choices.get(pk=request.POST['choice'])
            choice.vote()
        except(KeyError, Choice.DoesNotExist):
            context = {
                'poll': question,
                'message': 'Debes elegir una opción por favor...',
                'choices': question.choices.all()
            }
            return render(request, 'polls/detail.html', context)
        return redirect(reverse('polls:results', kwargs={'pk': question.pk}))


class QuestionResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.get_object().choices.all()
        context['choices'] = choices
        return context
