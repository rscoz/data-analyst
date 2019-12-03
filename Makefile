.PHONY: pipenv-setup
pipenv-setup:
	pipenv install

.PHONY: pipenv-active
pipenv-active:
	pipenv shell

.PHONY: pipenv-run
virtualenv-active:
	pipenv run .
