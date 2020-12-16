from django.urls import reverse

from behave import given, when, then

from apps.polls.factories import QuestionFactory

from pages import HomePage


@given('que se agregó la encuesta {text} y esta abierta')
def step_impl(context, text):
    context.poll = QuestionFactory(
        text=text,
        open=True
    )


@when('vaya al listado')
def step_impl(context):
    context.home_page = HomePage(context.browser)
    context.home_page.get(context.get_url(reverse('polls:index')))


@then('debe aparecer la encuesta {text}')
def step_impl(context, text):
    name = context.home_page.poll_title.text

    context.test.assertEqual(text, name)


# No hay encuestas abiertas

@given('que se agregó la encuesta {text} pero esta cerrada')
def step_impl(context, text):
    context.poll = QuestionFactory(
        text=text,
        open=False
    )


@then('debe decir {msj}')
def step_impl(context, msj):
    context.test.assertEqual(
        context.home_page.message.text,
        msj
    )
