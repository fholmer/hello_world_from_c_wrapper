#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#ifdef _WIN32
#  define EXPORT __declspec( dllexport )
#else
#  define EXPORT
#endif

EXPORT const char* hello_world(void);
EXPORT const char* hello(const char* name);
EXPORT const char* get_version_info(void);

#ifdef __cplusplus
}
#endif