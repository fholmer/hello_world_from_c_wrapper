#import pkg_resources
import ctypes
import os
#world_shared_object = pkg_resources.resource_filename(__name__, 'libworld.so')

pkg_dir = os.path.dirname(__file__)
for libfile in ['world.dll', 'libworld.so']:
    lib_path = os.path.join(pkg_dir, 'lib', libfile)
    print(libfile, lib_path, os.path.isfile(lib_path))
    if os.path.isfile(lib_path):
        ctypes.cdll.LoadLibrary(lib_path)
