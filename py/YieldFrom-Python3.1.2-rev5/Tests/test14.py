#
#   Test conversion of send(None) to next()
#

def g():
	yield from range(3)

gi = g()
for x in range(3):
	y = gi.send(None)
	print("Yielded:", y)
