run:
	@python manage.py runserver

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

test:
	@python manage.py test

coverage:
	@coverage run manage.py test
	@coverage report

test_e2e:
	@python manage.py behave
