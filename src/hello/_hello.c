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

static PyObject* _get_version_info(PyObject *self, PyObject *args) {
    return PyUnicode_FromString(get_version_info());
}

static PyMethodDef hello_methods[] = { 
    {   
        "hello_world", _hello_world, METH_NOARGS,
        "Print Hello, World!"
    },  
    {   
        "hello", _hello, METH_VARARGS,
        "Print Hello, name!"
    },  
    {   
        "get_version_info", _get_version_info, METH_NOARGS,
        "Get library version"
    },  
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hello_definition = { 
    PyModuleDef_HEAD_INIT,
    "hello",
    "A Hello world Python module.",
    -1, 
    hello_methods
};

PyMODINIT_FUNC PyInit__hello(void) {
    Py_Initialize();
    return PyModule_Create(&hello_definition);
}