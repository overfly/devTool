#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
os.system('chcp 65001')


def get_python_version():
    try:
        return os.popen("python --version".encode('utf-8').decode('gbk')).read()
    except ValueError:
        print(ValueError)


def get_maven_version():
    try:
        return os.popen("maven --version".encode('utf-8').decode('gbk')).read()
    except ValueError:
        print(ValueError)


print(get_python_version())
print(get_maven_version())
