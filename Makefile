setup:
	pip install -r requirements.txt

setup-dev: setup
	pip install -r requirements-dev.txt

lint:
	isort .
	black .
	flake8 .
	mypy .

test:
	pytest . -s --ignore-glob="*expensive/test_*.py"

test_:
	pytest . -s

all: lint test

all_: lint test_