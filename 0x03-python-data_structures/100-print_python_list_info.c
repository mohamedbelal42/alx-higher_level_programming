#include <python.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: PyObject list
 * Return:
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_Type(obj)->tp_name);
	}
}
