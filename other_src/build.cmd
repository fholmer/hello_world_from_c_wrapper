del world.dll
del world.exp
del world.lib
del world.obj

call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64
cl /LD world.c