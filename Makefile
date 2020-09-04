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

coverage_and_linter: lint
	@echo Pasando el coverage
	@coverage run manage.py test
	@coverage report

test_e2e:
	@python manage.py behave

lint:
	@echo Pasando el linter
	@flake8 apps/

rm:
	@rm -f -r .idea/
	@rm -f -r .vscode/
	@rm -f -r htmlcov/
