.PHONY: clean docs open-docs help test install-dev install
.DEFAULT_GOAL := help
SERVER_LOC = ''

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc ## remove all build and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

ifeq ($(OS), Windows_NT)

else
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
endif

clean-pyc: ## remove Python file artifacts
ifeq ($(OS), Windows_NT)

else
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
endif

lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

test: ## run tests quickly with the default Python
	$(MAKE) -C tests test

test-all: ## run tests on every Python version with tox
	tox

docs: ## generate Sphinx HTML documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

open-docs: docs ## Gnerate docs and display in browser
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist:
	pip-compile --extra-index-url $(SERVER_LOC) 
	pip install wheel 
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
ifeq ($(OS), Windows_NT)
	pip install --extra-index-url $(SERVER_LOC) -e .
else
	pip install --user --extra-index-url $(SERVER_LOC) -e .
endif

install-dev: clean ## install the package to the active Python's site-packages in editable mode with all the developer packages
ifeq ($(OS), Windows_NT)
	pip install --extra-index-url $(SERVER_LOC) -e .[dev]
else
	pip install --user --extra-index-url $(SERVER_LOC) -e .[dev]
endif
