#!/bin/sh

set -e

echo "Building"
make 

echo "Installing sdist"
pip install dist/sass-*.tar.gz

echo "Running tests"
#nosetests
nosetests --with-coverage

