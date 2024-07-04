import requests

def test_ok_1():
    requests.post('https://github.com/')

def test_ok_2():
    session = requests.Session()
    session.post('https://pastebin.com/')

def test_ok_3():
    with open('test_util.txt', 'rb') as f:
        s = requests.post('https://pastebin.com/', data=f)

def test_violation_1():
    with open('test_util.txt', 'r') as f:
        s = requests.post('https://github.com/', data=f)


def test_violation_3():
    with open('test_util.txt', 'r') as f:
        s = requests.post('https://github.com/', data=f)

def test_violation_2():
    with open('test_util.txt', 'r') as f:
        session = requests.Session()
        session.post('https://pastebin.com/', data=f)
