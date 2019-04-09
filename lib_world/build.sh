#ps: husk å lage mappen bin/linux hvis den ikke finnes

#slett fil hvis den finnes
test -e bin/linux/libworld.so && rm bin/linux/libworld.so

#kompiler fil
gcc -shared -o bin/linux/libworld.so -fPIC src/world.c
