#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>

#ifdef _WIN32
#  define EXPORT __declspec( dllexport )
#else
#  define EXPORT
#endif

EXPORT void hello_world(void);
EXPORT void hello(const char* name);

#ifdef __cplusplus
}
#endif