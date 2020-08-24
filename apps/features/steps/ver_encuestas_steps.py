from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import PollFactory


@given('que se agregó la encuesta {text} y esta abierta')
def step_impl(context, text):
    context.poll = PollFactory(
        text=text,
        open=True
    )


@when('vaya al listado')
def step_impl(context):
    context.browser.get(context.get_url(reverse('polls:index')))


@then('debe aparecer la encuesta {text}')
def step_impl(context, text):
    name = context.browser.find_element_by_tag_name('h4').text

    context.test.assertEqual(text, name)


# No hay encuestas abiertas

@given('que se agregó la encuesta {text} pero esta cerrada')
def step_impl(context, text):
    context.poll = PollFactory(
        text=text,
        open=False
    )


@then('debe decir {msj}')
def step_impl(context, msj):

    text = context.browser.find_element_by_tag_name('h4').text

    context.test.assertEqual(text, msj)
