from distutils.extension import Extension
from setuptools import setup, Extension
from Cython.Distutils import build_ext

import os.path
here = os.path.dirname(os.path.abspath(__file__))

ext_modules = [Extension("sass", 
					["sass.pyx"],
					libraries=["sass", 'stdc++']
				)]

setup(
  name = 'sass',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  version = '1.0',
  author = 'Sergey Kirilov',
  author_email = 'sergey.kirillov@gmail.com',
  url='https://github.com/pistolero/python-scss', 
  install_requires=['Cython'],
  license="Apache License 2.0",   
  keywords="sass scss libsass",  
  description='Python bindings for libsass',
  long_description=open(os.path.join(here, 'README.rst'), 'rb').read().decode('utf-8')    
)