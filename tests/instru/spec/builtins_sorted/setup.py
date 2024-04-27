from distutils.core import setup, Extension

module = Extension('customsorted', sources = ['customsorted.c'])

setup(name='customsorted',
      version='1.0',
      description='This module patches sorted().',
      ext_modules=[module])


# build with `python3 setup.py build_ext --inplace`
# then run any python script