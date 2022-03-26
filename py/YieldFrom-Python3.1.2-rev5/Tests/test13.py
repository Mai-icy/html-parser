#
#   Test delegation of next() to non-generator
#

def g():
	yield from range(3)

for x in g():
	print("Yielded", x)
