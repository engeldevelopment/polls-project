from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import ChoiceFactory, QuestionFactory

from pages import ResultPage

# Ver resultados de una encuesta cerrada


@given('la encuesta "{encuesta}" y está cerrada')
def step_impl(context, encuesta):
	context.question = QuestionFactory.create(
		text=encuesta,
		open=False
	)

	ChoiceFactory.create(
		text='Sí',
		poll=context.question
	)

	ChoiceFactory.create(
		text='No',
		poll=context.question
	)


@when('yo intente ver los resultados de dicha encuesta')
def step_impl(context):
	url = reverse('polls:results', kwargs={'pk': context.question.pk})
	context.result_page = ResultPage(context.browser)
	context.result_page.get(context.get_url(url))


@then('debe informarme "{msj}"')
def step_impl(context, msj):
	context.test.assertEqual(
		msj,
		context.result_page.message.text
	)

# Ver resultados de una encuesta sin opciones


@given('una encuesta "{encuesta}" sin opciones')
def step_impl(context, encuesta):
	context.question = QuestionFactory.create(
		text=encuesta,
		open=True
	)
