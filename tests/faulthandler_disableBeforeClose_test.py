import faulthandler
import signal
from nltk.tokenize import util
import sys
import io

def test_ok_1():
    # Register a handler for SIGUSR1 to dump the current thread's traceback
    faulthandler.enable(all_threads=False)
    faulthandler.disable()

def test_ok_2():
    # Setup the environment
    traceback_file_path = "traceback.log"

    # Open a file to write the traceback information
    f = open(traceback_file_path, "w")

    # Enable the fault handler with the specified file
    faulthandler.enable(file=f)

    faulthandler.disable()

    # correct usage: closing after disable
    f.close()


def test_violation_1():
    # Register a handler for SIGUSR1 to dump the current thread's traceback
    faulthandler.enable(all_threads=False)

    # misuse: closing before disable
    sys.stderr.close()

    faulthandler.disable()

def test_violation_2():
    # Setup the environment
    traceback_file_path = "traceback.log"

    # Open a file to write the traceback information
    f = open(traceback_file_path, "w")

    # Enable the fault handler with the specified file
    faulthandler.enable(file=f)

    # Register a handler for SIGUSR1 to dump the current thread's traceback
    faulthandler.enable(file=f, all_threads=False)

    # misuse: closing before disable
    f.close()

    faulthandler.disable()