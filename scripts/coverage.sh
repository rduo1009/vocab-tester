#!/bin/bash

echo -n "Running tests with coverage... "
coverage run tests/run_all_tests.py
echo "done"

echo -n "Generating coverage report... "
coverage html >> /dev/null
echo "done"
