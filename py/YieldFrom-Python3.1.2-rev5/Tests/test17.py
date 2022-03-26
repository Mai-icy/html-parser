#
#   Test attempting to send to non-generator
#

def g():
	try:
		print("starting g")
		yield from range(3)
		print("g should not be here")
	finally:
		print("finishing g")

gi = g()
next(gi)
for x in range(3):
	y = gi.send(42)
	print("Should not have yielded:", y)
