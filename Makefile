lint:
	flake8 .
	mypy .

format:
	black .
	isort .
