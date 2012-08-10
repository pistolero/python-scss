LDFLAGS="-Llibsass"

.PHONY: libsass

all: libsass ext

libsass:
	$(MAKE) -C $@

ext: sass.pyx setup.py
	LDFLAGS=$(LDFLAGS) python setup.py build

test: libsass ext
	LDFLAGS=$(LDFLAGS) python setup.py nosetests

clean:
	$(MAKE) -C libsass clean
	rm sass.c || true
	python setup.py clean

upload: all
	python setup.py sdist upload
