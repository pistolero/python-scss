from distutils.extension import Extension
from setuptools import setup, Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("sass", 
					["sass.pyx"],
					libraries=["sass", 'stdc++']
				)]

setup(
  name = 'sass',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)