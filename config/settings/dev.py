from .base import *

DEBUG = True

INSTALLED_APPS += [
    'behave_django',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('apps/db.sqlite3'),
    }
}
