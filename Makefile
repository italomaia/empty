.PHONY: all test

all: test

test:
	@python test_empty/runtests.py

clean: clean-pyc

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

tox-test:
	@tox
