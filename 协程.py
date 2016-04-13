#!/usr/bin/env python3
#antuor:Alan

import gevent

# def foo():
#     print('Running in foo !')
#     gevent.sleep(1)
#     print('Swith to foo again')
# def bar():
#     print('Runing to bar now !')
#     gevent.sleep(1)
#     print('Switch to bar again !')
# gevent.joinall(
#     [
#         gevent.spawn(foo),
#         gevent.spawn(bar),
#     ]
# )

# import gevent
#
# def task(pid):
#     """
#     Some non-deterministic task
#     """
#     gevent.sleep(0.5)
#     print('Task %s done' % pid)
#
# def synchronous():
#     for i in range(1,10):
#         task(i)
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(10)]
#     gevent.joinall(threads)
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()
# from gevent import monkey; monkey.patch_all()
# import gevent
# from  urllib.request import urlopen
#
# def f(url):
#     print('GET: %s' % url)
#     resp = urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))
#
# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://github.com/'),
# ])



import gevent.monkey
gevent.monkey.patch_socket()

import gevent
from  urllib.request import urlopen
import json

def fetch(pid):
    response = urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()