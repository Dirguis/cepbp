#!/usr/bin/env bash

TEST_PATH=tests/tests.py
echo "Running pre-commit hook"
pytest --verbose --color=yes $TEST_PATH

# $? stores exit value of the last command
if [ $? -ne 0 ]; then
 echo "Tests must pass before commit!"
 exit 1
fi
