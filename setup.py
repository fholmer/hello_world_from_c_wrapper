#!/usr/bin/env python3
# encoding: utf-8

import os
from setuptools import setup, Extension

# Answers to why variables must be different based on platform:

# rpath:
# in windows, this extension module will look for world.dll in its own directory.
# this is not the case in linux, but we can get it by putting the code $ ORIGIN in RUNPATH

# library_file:
# .dll libraries (windows) and .so libraries (linux) have different naming standards

# library_dir:
# ... and different placement based on build-scripts
 
if os.name == 'posix':
      rpath = ['$ORIGIN']
      library_file = 'libworld.so'
      library_dir = os.path.join('lib_world', 'bin', 'linux')
else:
      rpath = []
      library_file = 'world.dll'
      library_dir = os.path.join('lib_world', 'bin', 'win')

# and we need to attach the .dll or .so files as data in the setup file.
# into the same directory as our extension
data_files = os.path.join(library_dir, library_file)

include_dir = os.path.join('lib_world', 'include')

# build _hello.c
hello_ext_module = Extension(
      'hello.world._hello',
      sources=['src/hello/_hello.c'],
      include_dirs=[include_dir],
      library_dirs=[library_dir],
      libraries=['world'],
      runtime_library_dirs=rpath
      )

# put everything together
setup(name='hello',
      version='0.1.0',
      description='Hello world module written in C',
      packages=['hello', 'hello.world'],
      package_dir={'hello':'src/hello', 'hello.world':library_dir},
      package_data={'hello.world':[library_file]},
      ext_modules=[hello_ext_module])
