#
#   Test delegation of close() to non-generator
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
gi.close()
