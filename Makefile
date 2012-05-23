LDFLAGS="-Llibsass"

.PHONY: libsass

all: libsass ext

libsass:
	$(MAKE) -C $@

ext: sass.pyx setup.py
	LDFLAGS=$(LDFLAGS) python setup.py build

test: libsass ext
	LDFLAGS=$(LDFLAGS) python setup.py nosetests