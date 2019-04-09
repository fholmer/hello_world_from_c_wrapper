#!/usr/bin/env python3
# encoding: utf-8

import os
from setuptools import setup, find_packages, Extension

# i windows så vil denne extension-modulen lete etter world.dll i sin egen mappe.
# slik er det ikke i linux, men vi kan få det til ved å sette koden $ORIGIN i RUNPATH:
rpath = ['$ORIGIN'] if os.name == 'posix' else []

# .dll-biblioteker og .so biblioteker har forskjellig navnestandard:
library_file = 'libworld.so' if os.name == 'posix' else 'world.dll'

# og forskjellig plassering
library_dir = os.path.join('lib_world', 'bin', 'linux' if os.name == 'posix' else 'win')

# og vi må legge ved .dll eller .so filene som data i setupfilen.
# den må installeres i samme mappe som vår extension
data_files = os.path.join(library_dir, library_file)

#header filer
include_dir = os.path.join('lib_world', 'include')

hello_ext_module = Extension(
      'hello._hello',
      sources=['hello/_hello.c'],
      include_dirs=[include_dir],
      library_dirs=[library_dir],
      libraries=['world'],
      runtime_library_dirs=rpath
      )

setup(name='hello',
      version='0.1.0',
      description='Hello world module written in C',
      packages=find_packages(include=['hello']),
      data_files=[('hello', [data_files])],
      ext_modules=[hello_ext_module])

# kommentar til hello/hello.c:
#   husk at modulen må hete PyMODINIT_FUNC PyInit__hello(void) hvis du vil kalle den _hello. (underscore etter PyInit_)

# etter python setup.py install:
#   hvis du installerer så må du gå inn i en annen mappe (f.eks. env) for at _hello.py bootstrap skal virke
