# ============================== Define spec ==============================
from pythonmop import Spec, call
import threading
from pythonmop import instrumentation


class List_AppendOnce(Spec):
    """
    TODO: Add description here.
    """

    def __init__(self):
        super().__init__()

        @self.event_before(call(instrumentation.Instance, 'append_py'))
        def append_py(**kw):
            print("in append_py in monitor")

    ere = 'append_py append_py+'

    creation_events = ['append_py']

    def match(self, call_file_name, call_line_num):
        print(
            f'Spec - {self.__class__.__name__}: You should not call append_python more than once.'
            f'File {call_file_name}, line {call_line_num}.')
