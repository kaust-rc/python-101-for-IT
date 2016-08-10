#!/usr/bin/env python
"""
This is homework for class 2 and shouldnt take more than 1 hour,
but will help understand all we did in the last 2 classes
"""

import code2
from code2 import Demo2 as demoClass


def test_demo1():
    if code2.demo_function() != ("hello", "goodbye"):
        print "test_demo1 Failed"


def test_demo2():
    if demoClass.method1() != 1234:
        print "test1 failed!"


FAILED = list()

def test1():
    if code2.slice_list() != [2, 3, 4]:
        FAILED.append('test1')
        print "homework1 Failed", code2.slice_list()


def test2():
    """
    Note the 0, is not inside a list, while the 5 is!!
    """
    if code2.chop_list() != ([2, 3, 4],  0,  [5]):
        FAILED.append('test2')
        print "homework2 Failed", code2.chop_list()


def test3():
    """
    We did this on week 1
    """
    if code2.reverse_list() != [7, 6, 5, 4, 3, 2, 1]:
        FAILED.append('test3')
        print "homework3 Failed", code2.reverse_list()






def run_all_tests():
    test_demo1()
    test_demo2()
    test1()
    test2()
    test3()
    if FAILED == []:
        print "Congrats, all tests passed"


if __name__ == "__main__":
    run_all_tests()
