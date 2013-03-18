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

Development
-----------

Steps to compile and install:

::

   sudo pip install Cython
   git submodule init
   git submodule update
   make
   sudo python setup.py install

If you want to use an alternate `python`, you'll have to edit the `Makefile`.
