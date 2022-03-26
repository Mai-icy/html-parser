#
#   Test handling exception while delegating 'send'
#

def g1():
	print("Starting g1")
	x = yield "g1 ham"
	print("g1 received", x)
	yield from g2()
	x = yield "g1 eggs"
	print("g1 received", x)
	print("Finishing g1")

def g2():
	print("Starting g2")
	x = yield "g2 spam"
	print("g2 received", x)
	raise ValueError("hovercraft is full of eels")
	x = yield "g2 more spam"
	print("g2 received", x)
	print("Finishing g2")

g = g1()
y = next(g)
x = 1
try:
	while 1:
		y = g.send(x)
		print("Yielded", y)
		x += 1
except StopIteration:
	print("StopIteration")

