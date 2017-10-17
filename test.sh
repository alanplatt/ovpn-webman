#!/usr/bin/env bash

# Exit on any error
set -e


if [[ $TRAVIS != 'true' ]]; then

  VENV_NAME=".venv"
  if ! [ -e "${VENV_NAME}/bin/activate" ]; then
    echo "Creating virtualenv..."
    virtualenv -p python3 ${VENV_NAME}
  fi

  source "${VENV_NAME}/bin/activate"

  echo "Installing requirements..."
  pip install -q -r requirements.txt -r requirements-tests.txt

fi

echo "Cleaning .pyc files..."
find . -iname "*.pyc" -delete

echo "Running tests..."
python -m pytest tests/
#pytest tests
#nosetests --with-coverage --cover-erase --cover-package=aws_assume_role

echo "Running flake8..."
flake8 *.py

echo "Done!!"
