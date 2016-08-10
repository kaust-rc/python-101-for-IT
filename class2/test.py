#!/usr/bin/env python

#from filename import function1, function2
from mymodule import mycode, uname


#import filename as alias
import mymodule as anothercode

#import differentdirectory.code

def exe1():
    """
    This demonstrates running the code with "from mymodule import mycode"
    """
    mycode()
    uname()


def exe2():
    """
    This demonstrates, "import mymodule as alias"
    """
    anothercode.mycode()
    anothercode.uname()


if __name__ == "__main__":
    exe1()
    exe2()
