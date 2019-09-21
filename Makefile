TEST_PATH=tests/tests.py

.PHONY: clean-pyc_1 clean-pyc_2 test run-test init

tests: clean-pyc_1 run-test clean-pyc_2

clean-pyc_1:
	find . -name '*.pyc' -delete

clean-pyc_2:
	find . -name '*.pyc' -delete

run-test:
	pytest --verbose --color=yes $(TEST_PATH)

init:
	pip install -r requirements.txt
