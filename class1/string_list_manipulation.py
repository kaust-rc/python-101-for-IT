"""
String manipulation
This is something very basic in python but will be used a lot!!!
"""

#This is a string from a uname output  copy this into "ipython" and type in the below text
uname = "'Darwin kl-14681 15.6.0 Darwin Kernel Version 15.6.0: Thu Jun 23 18:25:34 PDT 2016; root:xnu-3248.60.10~1/RELEASE_X86_64 x86_64'"

#Selects the first character.
#Note the second single quote, is the first charactor
uname[0]

#Takes from the first item to the 6th item
uname[1:7]

#Takes every second charactor
uname[::2]

#Split splits the string on a space
uname.split(' ')

#Split splits the string on a space, space is the default
uname.split()

#Returns 'Darwin' the first item on the list.  The list is the string split
#on spaces
uname.split(' ')[0]

#Returns 'arwin'
uname.split(' ')[0][1:]

#makes a list from 0-9, ie ten items
range(10)

#makes a list from 5-9, ie 4 items
range(5,10)

#To make a string with internal quotes
string_with_internal_quotes = "a\""
string_with_internam_quotes = "a'"
string_with_internal_quotes = """a''adf'''";;"""

#Try guess what these will return before running them
pwd = '/Users/obyrnenp/workspace/py-IT/1'
pwd.split()[-1]
pwd.split('/')[-1]

alist = ['fist', 'second', 'third']
alist[0]
alist[-1]
alist[2]
