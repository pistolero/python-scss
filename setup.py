#   Copyright 2012 Sergey Kirillov
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from distutils.extension import Extension
from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
except ImportError:
    print("No Cython installed. Building from pregenerated C source.")
    build_ext = None

import os.path
here = os.path.dirname(os.path.abspath(__file__))

libsass_sources = [
    'libsass/ast.cpp',
    'libsass/base64vlq.cpp',
    'libsass/bind.cpp',
    'libsass/constants.cpp',
    'libsass/context.cpp',
    'libsass/contextualize.cpp',
    'libsass/copy_c_str.cpp',
    'libsass/emscripten_wrapper.cpp',
    'libsass/error_handling.cpp',
    'libsass/eval.cpp',
    'libsass/expand.cpp',
    'libsass/extend.cpp',
    'libsass/file.cpp',
    'libsass/functions.cpp',
    'libsass/inspect.cpp',
    'libsass/output_compressed.cpp',
    'libsass/output_nested.cpp',
    'libsass/parser.cpp',
    'libsass/prelexer.cpp',
    'libsass/sassc++.cpp',
    'libsass/sass.cpp',
    'libsass/sass_interface.cpp',
    'libsass/source_map.cpp',
    'libsass/test_paths.cpp',
    'libsass/test_selector_difference.cpp',
    'libsass/test_specificity.cpp',
    'libsass/test_subset_map.cpp',
    'libsass/test_superselector.cpp',
    'libsass/test_unification.cpp',
    'libsass/to_c.cpp',
    'libsass/to_string.cpp',
    'libsass/trim.cpp',
    'libsass/units.cpp'
]

ext_modules = [Extension("sass", 
               libsass_sources + ["sass.pyx"],
               libraries=['stdc++'],
               library_dirs=['./libsass'],
               include_dirs=['.', 'libsass'],
               language='c++'
)]

cmdclass = {}
if build_ext:
    cmdclass = {'build_ext': build_ext}


setup(
  name = 'sass',
  cmdclass = cmdclass,
  ext_modules = ext_modules,
  version = '2.0',
  author = 'Sergey Kirilov',
  author_email = 'sergey.kirillov@gmail.com',
  url='https://github.com/pistolero/python-scss', 
  install_requires=[],
  extras_require = {
#    'develop': ['Cython']
  },
  license="Apache License 2.0",   
  keywords="sass scss libsass",  
  description='Python bindings for libsass',
  long_description=open(os.path.join(here, 'README.rst'), 'rb').read().decode('utf-8')    
)
