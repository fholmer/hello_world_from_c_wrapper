:: ps husk å lage mappen bin/win hvis den ikke finnes
if not exist bin mkdir bin
if not exist bin\win mkdir bin\win
::del bin\win\*

call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64
cl /LD -Fe:bin/win/world -Fo:bin/win/world src/world.c
