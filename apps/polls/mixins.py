from .models import Question

from .utils import make_context_for


class QuestionDetailViewMixin(object):
    model = Question
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        make_context_for(question, context)
        return context
