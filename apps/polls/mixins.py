from .models import Question


class QuestionDetailViewMixin(object):
    model = Question
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()

        errors = []
        if not question.open:
            errors.append('Esta encuesta está cerrada.')

        if not question.has_choices():
            errors.append('De esta encuesta no hay resultados que mostrar.')

        choices = question.choices.all()
        context['errors'] = errors
        context['choices'] = choices
        return context
