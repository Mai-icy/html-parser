#
#   Test grammar and code generation
#

import dis

def g1():
	yield
	yield 42

def g2():
	yield from x

def g3():
	x = yield from x

def disgen(g):
	print("---------- %s ----------" % g.__name__)
	dis.dis(g)

disgen(g1)
disgen(g2)
disgen(g3)
