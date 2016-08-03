#!/usr/bin/env python

from ping import ping_time


def test_ping():
	if ping_time():
		print "Ping sucessfull"

	else:
		print "Ping unsuccessful"


if __name__=="__main__":
    test_ping()
