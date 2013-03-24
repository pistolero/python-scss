#!/bin/sh

set -e

echo "Cythoning saas.pyx"
cython sass.pyx

echo "Building sdist"
python setup.py sdist

echo "Installing sdist"
pip install dist/sass-*.tar.gz

echo "Running tests"
nosetests
