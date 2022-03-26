#
#   Test delegating 'throw' to non-generator
#

def g():
	try:
		print("Starting g")
		yield from range(10)
	finally:
		print("Finishing g")

gi = g()
for i in range(5):
	x = next(gi)
	print("Yielded", x)
e = ValueError("tomato ejected")
gi.throw(e)
