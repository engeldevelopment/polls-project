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
    context.browser.get(context.get_url(reverse('polls:index')))

    context.browser.find_element_by_css_selector('a[data-encuesta]').click()

    context.browser.find_element_by_id('btn-votar').click()


@then('me dirá "{msj}"')
def step_impl(context, msj):
    text = context.browser.find_element_by_tag_name('p[data-msj]').text

    context.test.assertEqual(msj, text)


# Realizar votación

@when('vote por la opción Sí')
def step_impl(context):
    context.browser.get(context.get_url(context.question.get_absolute_url()))

    value = 'label[for="{}"]'.format(context.si.pk)
    context.browser.find_element_by_css_selector(value).click()
    context.browser.find_element_by_id('btn-votar').click()


@then('me debe mostrar los resultados')
def step_impl(context):

    titulo = context.browser.find_element_by_tag_name('h2').text
    h4 = context.browser.find_element_by_tag_name('h4').text

    context.test.assertEqual('Los Venezolanos son Flojos', titulo)
    context.test.assertEqual('Resultados', h4)
