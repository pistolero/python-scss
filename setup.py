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
    print "No Cython installed. Building from pregenerated C source."
    build_ext = None

import os.path
here = os.path.dirname(os.path.abspath(__file__))



ext_modules = [Extension("sass", 
               ["sass.pyx"],
               libraries=["sass", 'stdc++'],
               library_dirs=['./libsass']
)]

cmdclass = {}
if build_ext:
    cmdclass = {'build_ext': build_ext}


setup(
  name = 'sass',
  cmdclass = cmdclass,
  ext_modules = ext_modules,
  version = '1.2',
  author = 'Sergey Kirilov',
  author_email = 'sergey.kirillov@gmail.com',
  url='https://github.com/pistolero/python-scss', 
  install_requires=['Cython'],
  license="Apache License 2.0",   
  keywords="sass scss libsass",  
  description='Python bindings for libsass',
  long_description=open(os.path.join(here, 'README.rst'), 'rb').read().decode('utf-8')    
)
