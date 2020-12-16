from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import QuestionFactory, ChoiceFactory

from pages import HomePage, PollPage


@given('que hay una encuesta llamada {name}')
def step_impl(context, name):
    context.poll = QuestionFactory.create(text=name)


@given('le agregaron las opciones {si} y {no}')
def step_impl(context, si, no):
    ChoiceFactory.create(text=si, poll=context.poll)
    ChoiceFactory.create(text=no, poll=context.poll)


@when('vaya a la encuesta')
def step_impl(context):
    context.home_page = HomePage(context.browser)
    context.home_page.get(context.get_url(reverse('polls:index')))
    context.home_page.link_to_poll.click()


@then('podré ver sus opciones {si} y {no}')
def step_impl(context, si, no):
    poll_page = PollPage(context.browser)
    opciones = poll_page.options.text

    context.test.assertIn(opciones, si)
    context.test.assertIn(opciones, no)
