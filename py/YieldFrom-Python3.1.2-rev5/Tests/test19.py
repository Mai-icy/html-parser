#
#   Test attempted yield-from loop
#

def g1():
	print("g1: starting")
	yield "y1"
	print("g1: about to yield from g2")
	yield from g2()
	print("g1 should not be here")

def g2():
	print("g2: starting")
	yield "y2"
	print("g2: about to yield from g1")
	yield from gi
	print("g2 should not be here")

gi = g1()
for y in gi:
	print("Yielded:", y)
