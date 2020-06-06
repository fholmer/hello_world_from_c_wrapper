:: create folder if not exist
if not exist bin mkdir bin
if not exist bin\win mkdir bin\win

:: setup environment
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64

:: build
cl /LD -Fe:bin/win/world -Fo:bin/win/world src/world.c
