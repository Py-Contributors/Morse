#!/bin/sh

# check if the flake8 and pytest are installed
if [ ! -x "$(command -v flake8)" ]; then
    echo "flake8 is not installed"
    exit 1
fi

if [ ! -x "$(command -v pytest)" ]; then
    echo "pytest is not installed"
    exit 1
fi

# run flask8 and pytest

flake8 
pytest -e 

