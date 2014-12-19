#!/usr/bin/env python
"""
letters.py

A group of personal hello_world functions
"""

from __future__ import print_function
from datetime import date


def hello_world():
    print("Hello world!  Today's date is: {0}".format(date.today()))

def goodbye_world():
    print("Goodbye world!")


def hello_joe(my_str):
    print("Hello Joe:  {0}".format(my_str))

def hello_oriana(my_str):
    print("Hello Oriana!: {0}".format(my_str))

def hello_diana(my_str):
    print("Hello Diana!: {0}".format(my_str))
