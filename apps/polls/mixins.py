from .models import Question


class QuestionDetailViewMixin(object):
    model = Question
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.get_object().choices.all()
        context['choices'] = choices
        return context
