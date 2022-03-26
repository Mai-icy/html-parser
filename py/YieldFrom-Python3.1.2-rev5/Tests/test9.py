#
#   Test handling exception while delegating 'close'
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
		yield "g2 more spam"
	finally:
		print("Finishing g2")
		raise ValueError("nybbles have exploded with delight")

g = g1()
for i in range(2):
	x = next(g)
	print("Yielded", x)
g.close()
