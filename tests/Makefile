.PHONY: clean help test
.DEFAULT_GOAL := help

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

clean:  ## remove all test, coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr __pycache__
	rm -fr pytest_output

test: clean
	python -m pytest --verbose
	python -m coverage html