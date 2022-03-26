#
#   Test delegation of initial next() call to subgenerator
#

def g1():
	print("Starting g1")
	yield from g2()
	print("Finishing g1")

def g2():
	print("Starting g2")
	yield 42
	print("Finishing g2")

for x in g1():
	print("Yielded", x)
