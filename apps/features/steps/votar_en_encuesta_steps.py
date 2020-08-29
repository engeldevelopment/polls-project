from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import ChoiceFactory, QuestionFactory


@given('que está la encuesta {encuesta}')
def step_impl(context, encuesta):
    context.question = QuestionFactory.create(
        text=encuesta
    )


@given('tiene las opciones {si} y {no}')
def step_impl(context, si, no):
    ChoiceFactory.create(
        text=si,
        poll=context.question
    )
    ChoiceFactory.create(
        text=no,
        poll=context.question
    )


@when('intente votar sin elegir una de las opciones')
def step_impl(context):
    context.browser.get(context.get_url(reverse('polls:index')))

    context.browser.find_element_by_css_selector('a[data-encuesta]').click()

    context.browser.find_element_by_id('btn-votar').click()


@then('me dirá "{msj}"')
def step_impl(context, msj):
    text = context.browser.find_element_by_tag_name('p[data-msj]').text

    context.test.assertEqual(msj, text)
