:: ps husk å lage mappen bin/win hvis den ikke finnes

del bin/win/world.dll
del world.exp
del bin/win/world.lib
del world.obj

call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64
cl /LD world.c
move world.dll bin/win/
move world.lib bin/win/