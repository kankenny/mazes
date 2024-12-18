setup:
	pip install -r requirements.txt

setup-dev: setup
	pip install -r requirements-dev.txt

lint:
	isort .
	black .
	flake8 .

test:
	pytest .

all: lint test