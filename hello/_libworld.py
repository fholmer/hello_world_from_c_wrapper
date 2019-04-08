#import pkg_resources
import ctypes
import os
#world_shared_object = pkg_resources.resource_filename(__name__, 'libworld.so')

pkg_dir = os.path.dirname(__file__)
lib_file = os.path.join(pkg_dir, 'libworld.so')
print(lib_file)
ctypes.cdll.LoadLibrary(lib_file)

