#include "../include/world.h"

const char* hello_world() {
    return "Hello, world!\n";
}

const char* hello(const char* name) {
    char * reply = malloc(strlen(name) + 10);
    sprintf(reply, "Hello, %s!\n", name);
    return reply;
}

const char* get_version_info() {
    return "1.0.0-RC1";
}