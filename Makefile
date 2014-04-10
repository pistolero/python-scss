LDFLAGS="-Llibsass"

all: libsass ext

ext: sass.pyx setup.py
	cython --cplus sass.pyx
	python setup.py build 
	python setup.py sdist

test: libsass ext
	nosetests

clean:
	rm sass.cpp || true
	rm -r build
	python setup.py clean

dist: all test

upload: dist
	python setup.py upload
