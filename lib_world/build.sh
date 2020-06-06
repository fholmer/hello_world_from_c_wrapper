# create folder if not exist
mkdir -p bin/linux

# remove previous build
test -e bin/linux/libworld.so && rm bin/linux/libworld.so

# build
gcc -shared -o bin/linux/libworld.so -fPIC src/world.c
