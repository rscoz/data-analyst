.PHONY: pipenv-setup
pipenv-setup:
	pipenv install -d

.PHONY: run
run:
	pipenv run python app.py
