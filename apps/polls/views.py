from django.views import generic
from .models import Poll


class PollListView(generic.ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.filter(open=True)
