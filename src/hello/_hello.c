#include <stdio.h>
#include <Python.h>
#include <world.h>

// Module method definitions
static PyObject* _hello_world(PyObject *self, PyObject *args) {
    PySys_FormatStdout("%s", hello_world());
    Py_RETURN_NONE;
}

static PyObject* _hello(PyObject *self, PyObject *args) {
    const char* name;
    if (!PyArg_ParseTuple(args, "s", &name)) {
        return NULL;
    }
    PySys_FormatStdout("%s", hello(name));
    Py_RETURN_NONE;
}

static PyMethodDef hello_methods[] = { 
    {   
        "hello_world", _hello_world, METH_NOARGS,
        "Print 'hello world' from a method defined in a C extension."
    },  
    {   
        "hello", _hello, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },  
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hello_definition = { 
    PyModuleDef_HEAD_INIT,
    "hello",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    hello_methods
};

PyMODINIT_FUNC PyInit__hello(void) {
    Py_Initialize();
    return PyModule_Create(&hello_definition);
}