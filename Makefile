.PHONY: postgres
postgres:
	docker run -p 5432:5432 -e POSTGRES_USER=read-only-user -e POSTGRES_PASSWORD=stone123 -d postgres

.PHONY: pipenv-setup
pipenv-setup:
	pipenv install

.PHONY: pipenv-active
pipenv-active:
	pipenv shell

.PHONY: pipenv-run
virtualenv-active:
	pipenv run .
