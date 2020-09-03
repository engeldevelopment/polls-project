def make_context_for(question, context):
    errors = []
    if not question.open:
        errors.append('Esta encuesta está cerrada.')

    if not question.has_choices():
        errors.append('De esta encuesta no hay resultados que mostrar.')

    choices = question.choices.all()
    context['errors'] = errors
    context['choices'] = choices
    return context
