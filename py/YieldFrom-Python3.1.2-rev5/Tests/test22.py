#
#  Test send and return with value
#

def f(r):
	gi = g(r)
	next(gi)
	try:
		print("f sending spam to g")
		gi.send("spam")
		print("f SHOULD NOT BE HERE")
	except StopIteration as e:
		print("f caught", repr(e))

def g(r):
	print("g starting")
	x = yield
	print("g received", x)
	print("g returning", r)
	return r

f(None)
f(42)
