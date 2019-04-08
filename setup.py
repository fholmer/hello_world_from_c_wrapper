#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup, find_packages, Extension

hello_ext_module = Extension(
      'hello._hello',
      sources=['hello/_hello.c'],
      include_dirs=['other_src'],
      library_dirs=['other_src'],
      libraries=['world']
      #runtime_library_dirs=['.']
      )

setup(name='hello',
      version='0.1.0',
      description='Hello world module written in C',
      packages=find_packages(include=['hello']),
      data_files=[('hello',['other_src/libworld.so'])],
      ext_modules=[hello_ext_module])

# husk at modulen må hete PyMODINIT_FUNC PyInit__hello(void) hvis du vil kalle den _hello. (underscore!)
# hvis du installerer så må du gå inn i en annen mappe (f.eks. env) for at _hello.py bootstrap skal virke

