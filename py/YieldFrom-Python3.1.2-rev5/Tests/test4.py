#
#   Test delegation of next() call to subgenerator


def g1():
	print("Starting g1")
	yield "g1 ham"
	yield from g2()
	yield "g1 eggs"
	print("Finishing g1")

def g2():
	print("Starting g2")
	yield "g2 spam"
	yield "g2 more spam"
	print("Finishing g2")

for x in g1():
	print("Yielded", x)
