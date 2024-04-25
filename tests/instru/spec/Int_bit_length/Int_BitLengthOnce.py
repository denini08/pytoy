# ============================== Define spec ==============================
from pythonmop import Spec, call
import threading
from pythonmop import instrumentation
import customint

customint.install_custom_bit_length()

class Int_BitLengthOnce(Spec):
    """
    TODO: Add description here.
    """

    def __init__(self):
        super().__init__()

        @self.event_before(call(instrumentation, 'bit_length_py_instance'))
        def bit_length_py(**kw):
            print("in bit_length_py in monitor")

    ere = 'bit_length_py bit_length_py+'

    creation_events = ['bit_length_py']

    def match(self, call_file_name, call_line_num):
        print(
            f'Spec - {self.__class__.__name__}: You should not call bit_length_py more than once.'
            f'File {call_file_name}, line {call_line_num}.')


spec_instance = Int_BitLengthOnce()
spec_instance.create_monitor("Int_BitLengthOnce")


n = -37
bin(n)
n.bit_length()
n.bit_length()