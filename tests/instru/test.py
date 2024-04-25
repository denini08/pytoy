from pythonmop.instrumentation import append_py_instance


def test01():
    print("Hello, World!")
    append_py_instance(1, 2)
    append_py_instance(1, 44)
