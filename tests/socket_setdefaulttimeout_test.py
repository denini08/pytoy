import socket

def test_ok_1():
    assert 1 == 1


def test_ok_2():
    socket.setdefaulttimeout(None)

def test_ok_3():
    socket.setdefaulttimeout(0)

def test_ok_4():
    socket.setdefaulttimeout(2.4)

def test_not_ok_1():
    socket.setdefaulttimeout(-3)

def test_not_ok_2():
    socket.setdefaulttimeout(-3.4)