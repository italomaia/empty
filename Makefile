.PHONY: all test

all: test

test:
	@python setup.py test

publish:
	@python setup.py sdist upload

clean: clean-pyc

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

tox-test:
	@tox
