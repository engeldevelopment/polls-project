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
        choices = Choice.objects.filter(poll__pk=self.kwargs['pk'])
        context['choices'] = choices
        return context
