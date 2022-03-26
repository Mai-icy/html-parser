#
#   Test raising exception in delegated next() call
#

def g1():
	try:
		print("Starting g1")
		yield "g1 ham"
		yield from g2()
		yield "g1 eggs"
	finally:
		print("Finishing g1")

def g2():
	try:
		print("Starting g2")
		yield "g2 spam"
		raise ValueError("hovercraft is full of eels")
		yield "g2 more spam"
	finally:
		print("Finishing g2")

for x in g1():
	print("Yielded", x)
