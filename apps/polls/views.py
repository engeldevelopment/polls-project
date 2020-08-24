from django.views import generic
from .models import Poll, Choice


class PollListView(generic.ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.open()


class PollDetailView(generic.DeleteView):
    model = Poll
    template_name = 'polls/detail.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = Choice.objects.filter(poll__pk=self.kwargs['pk'])
        context['choices'] = choices
        return context
