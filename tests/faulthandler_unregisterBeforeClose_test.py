import faulthandler
import signal
from nltk.tokenize import util
import sys
import io

def test_ok_1():
    # Register a handler for SIGUSR1 to dump the current thread's traceback
    faulthandler.register(signum=signal.SIGUSR1, all_threads=False)
    faulthandler.unregister(signal.SIGUSR1)

def test_ok_2():
    # Setup the environment
    traceback_file_path = "traceback.log"

    # Open a file to write the traceback information
    f = open(traceback_file_path, "w")

    # Enable the fault handler with the specified file
    faulthandler.enable(file=f)

    # Register a handler for SIGUSR1 to dump the current thread's traceback
    faulthandler.register(signal.SIGUSR1, file=f, all_threads=False)

    faulthandler.unregister(signal.SIGUSR1)

    # correct usage: closing after unregister
    f.close()


# def test_violation_1():
#     # Register a handler for SIGUSR1 to dump the current thread's traceback
#     faulthandler.register(signum=signal.SIGUSR1, all_threads=False)

#     # misuse: closing before unregister
#     sys.stderr.close()

#     faulthandler.unregister(signal.SIGUSR1)

# def test_violation_2():
#     # Setup the environment
#     traceback_file_path = "traceback.log"

#     # Open a file to write the traceback information
#     f = open(traceback_file_path, "w")

#     # Enable the fault handler with the specified file
#     faulthandler.enable(file=f)

#     # Register a handler for SIGUSR1 to dump the current thread's traceback
#     faulthandler.register(signal.SIGUSR1, file=f, all_threads=False)

#     # misuse: closing before unregister
#     f.close()

#     faulthandler.unregister(signal.SIGUSR1)