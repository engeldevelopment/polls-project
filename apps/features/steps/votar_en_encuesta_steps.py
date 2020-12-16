from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import ChoiceFactory, QuestionFactory
from pages import HomePage, PollPage, ResultPage


@given('que está la encuesta {encuesta}')
def step_impl(context, encuesta):
    context.question = QuestionFactory.create(
        text=encuesta
    )


@given('tiene las opciones {si} y {no}')
def step_impl(context, si, no):
    context.si = ChoiceFactory.create(
        text=si,
        poll=context.question
    )
    ChoiceFactory.create(
        text=no,
        poll=context.question
    )


@when('intente votar sin elegir una de las opciones')
def step_impl(context):
    context.home_page = HomePage(context.browser)
    context.poll_page = PollPage(context.browser)

    context.home_page.get(context.get_url(reverse('polls:index')))

    context.home_page.link_to_poll.click()

    context.poll_page.btn_vote.click()


@then('me dirá "{msj}"')
def step_impl(context, msj):
    context.test.assertEqual(msj, context.poll_page.message.text)


# Realizar votación

@when('vote por la opción Sí')
def step_impl(context):
    context.poll_page = PollPage(context.browser)
    context.poll_page.get(context.get_url(context.question.get_absolute_url()))

    value = 'label[for="{}"]'.format(context.si.pk)
    context.browser.find_element_by_css_selector(value).click()
    context.poll_page.btn_vote.click()


@then('me debe mostrar los resultados')
def step_impl(context):
    result_page = ResultPage(context.browser)

    context.test.assertEqual(
        'Los Venezolanos son Flojos',
        result_page.title.text
    )
    context.test.assertEqual('Resultados', result_page.subtitle.text)
