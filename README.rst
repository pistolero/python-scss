Python binding for libsass
==========================

|BuildStatus|

.. |BuildStatus| image:: https://secure.travis-ci.org/pistolero/python-scss.png?branch=master
                 :target: http://github.com/pistolero/python-scss/
                 :alt: Build status

Usage
-----

::

   >>> import sass
   >>> sass.compile_string("div { a { color: black}}")
   'div a {\n  color: black; }\n'


Installation
------------

::
    pip install sass


Compatibility
-------------

Tested with Python 2.7 and Python 3.2/3.3


Development
-----------

Steps to compile and install:

::

   sudo pip install Cython
   git submodule init
   git submodule update
   make
   sudo python setup.py install

If you want to use an alternate `python`, you'll have to edit the `Makefile` or execute those commands from activated virtualenv.
