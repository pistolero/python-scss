LDFLAGS="-Llibsass"

all: libsass ext

ext: sass.pyx setup.py
	LDFLAGS=$(LDFLAGS) python setup.py build

test: libsass ext
	LDFLAGS=$(LDFLAGS) python setup.py nosetests

clean:
	rm sass.c || true
	python setup.py clean

upload: all
	python setup.py sdist upload
