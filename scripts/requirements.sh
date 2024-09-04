#!/bin/bash

poetry export --format=requirements.txt --output=requirements.txt --without-hashes --without-urls  
poetry export --format=requirements.txt --output=requirements-dev.txt --without-hashes --without-urls --with=dev    