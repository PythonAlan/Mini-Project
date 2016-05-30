#!/usr/bin/env python3
#antuor:Alan



from setuptools import setup

APP = ['售价计算器.py']
DATA_file = ['settings']
OPTIONS = {'iconfile':'hacker.icns'}

setup(
    app = APP,
    data_file = DATA_file,
    setup_requires = ['py2app'],
    options = {'py2app':OPTIONS},
)
