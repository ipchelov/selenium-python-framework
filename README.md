# Python Selenium UI test framework
This is an example of organizing a test framework for UI using the following tools:
 - pytest
 - selenium
 - allure
 - PyHamcrest
 - flake8, isort, black, mypy

The IKEA website is used as an instance of the target site

Verified for Linux

## Requirements
 - python 3.12
 - Chrome Browser
 - chromedriver, chromedriver is in the PATH
 - Firefox Browser
 - geckodriver, geckodriver is in the PATH

## Installation
From project root directory:
```
python3.12 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
## Setup and Run
Set up driver settings in the ```core/settings/driver_settings.py```

Run:
```
pytest
```
Run with Allure results:

```
pytest --alluredir=./allure_results
allure serve allure_results/
```

## Linters and Formatters
```make``` tool is required to be installed. From project root directory:

Linters (flake8, mypy)
```
make lint
```
Formatters (black, isort)

```
make format
```

## Comments on the framework
The framework provides an overview of solutions to various problems encountered in the development of UI testing automation

Not all methods from the BaseElement, AssertThat and AssertThatString classes are used in the tests themselves, but they are present to show the logic of working with the relevant parts and how they can be developed