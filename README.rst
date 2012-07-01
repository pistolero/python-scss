Python binding for libsass
==========================

[![Build Status](https://secure.travis-ci.org/pistolero/python-scss.png?branch=master)](http://github.com/pistolero/python-scss/)

Usage
-----

::

   >>> import sass
   >>> sass.compile_string("div { a { color: black}}")
   'div a {\n  color: black; }\n'

