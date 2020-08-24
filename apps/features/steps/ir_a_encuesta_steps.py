from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import PollFactory, ChoiceFactory


@given('que hay una encuesta llamada {name}')
def step_impl(context, name):
    context.poll = PollFactory.create(text=name)


@given('le agregaron las opciones {si} y {no}')
def step_impl(context, si, no):

    ChoiceFactory.create(text=si, poll=context.poll)
    ChoiceFactory.create(text=no, poll=context.poll)


@when('vaya a la encuesta')
def step_impl(context):

    context.browser.get(context.get_url(reverse('polls:index')))

    context.browser.find_element_by_css_selector('a[data-encuesta]').click()


@then('podré ver sus opciones {si} y {no}')
def step_impl(context, si, no):

    opciones = context.browser.find_element_by_css_selector('input[type="radio"]').text

    context.test.assertIn(opciones, si)
    context.test.assertIn(opciones, no)
