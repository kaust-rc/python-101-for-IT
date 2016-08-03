#!/usr/bin/env python


def my_function(text):
    """
    This is the function I want to code
    """
    return text




def test():
    """
    This is a simple test, to show it works
    """
    if my_function('hello') == "hello":
        print "Test 1 pass"
    else:
        print "Test 1 failed"

    #A second test to see if it works with a number
    if my_function(9999) == 9999:
        print "Test 2 pass"
    else:
        print "Test 2 failed"


if __name__=="__main__":
    test()




