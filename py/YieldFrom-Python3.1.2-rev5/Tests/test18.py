#
#   Test exception in initial next() call
#

def g1():
	print("g1 about to yield from g2")
	yield from g2()
	print("g1 should not be here")

def g2():
	yield 1/0

gi = g1()
next(gi)
