#!/bin/bash

# From https://github.com/python-poetry/poetry-plugin-export/issues/183#issuecomment-1804931339

poetry install --only main --sync
poetry run pip freeze > requirements.txt

poetry install --sync
poetry run pip freeze > requirements-dev.txt