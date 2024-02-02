import sys
import pytest

# this tests are broking the other test
# remove this line to run the tests
pytest.skip("Skipping console_close_reader_test.py", allow_module_level=True)


def test_ok_1():
    assert 1 == 1


def test_violation_1():
    sys.stdout.close()
