.PHONY: pipenv-setup
pipenv-setup:
	pipenv install

.PHONY: pipenv-active
pipenv-active:
	pipenv shell

.PHONY: pipenv-run
pipenv-run:
	pipenv run .
