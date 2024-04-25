# # ============================== Define spec ==============================
# from pythonmop import Spec, call
# import threading
# from pythonmop import instrumentation
# from pythonmop.instrumentation import append_py_instance

# import customlist



# class List_AppendOnce(Spec):
#     """
#     TODO: Add description here.
#     """

#     def __init__(self):
#         super().__init__()

#         @self.event_before(call(instrumentation, 'append_py_instance'))
#         def append_py(**kw):
#             print("in append_py in monitor")
#             customlist.install_custom_append()

#     ere = 'append_py append_py+'

#     creation_events = ['append_py']

#     def match(self, call_file_name, call_line_num):
#         print(
#             f'Spec - {self.__class__.__name__}: You should not call append_python more than once.'
#             f'File {call_file_name}, line {call_line_num}.')


# spec_instance = List_AppendOnce()
# spec_instance.create_monitor("List_AppendOnce")

# print('imported customlist')

# customlist.install_custom_append()

# a = []
# a.append(1)
# # append_py_instance(2)

# # append_py_instance(1, 2)
# # append_py_instance(1, 44)