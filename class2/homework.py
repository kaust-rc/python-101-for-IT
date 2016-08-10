#/usr/bin/env python
"""
This is homework for class 2 and shouldnt take more than 1 hour,
but will help understand all we did in the last 2 classes
"""

import myhomework
from myhomework import Demo2 as demoClass


def test_demo():
    if demo1 != ("hello", "goodbye"):
        print "test_demo Failed"


def test_demo2():
    if demoClass.method1() != 1234:
        print "test1 failed!"


def test1():
    if myhomework.slice_list() != [2, 3, 4]:
        print "homework1 Failed", myhomework.slice_list()


def test2():
    """
    Note the 0, is not inside a list, while the 5 is!!
    """
    if myhomework.chop_list() != ([2, 3, 4],  0,  [5]):
        print "homework2 Failed", myhomework.chop_list()


def test3():
    """
    We did this on week 1
    """
    if myhomework.reverse_list() != [7, 6, 5, 4, 3, 2, 1]:
        print "homework3 Failed", myhomework.reverse_list()






def run_all_tests():
    test1()
    test2()
    test3()



if __name__ == "__main__":
    run_all_tests()
