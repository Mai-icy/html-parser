#
#  Test next and return with value
#

def f(r):
	gi = g(r)
	next(gi)
	try:
		print("f resuming g")
		next(gi)
		print("f SHOULD NOT BE HERE")
	except StopIteration as e:
		print("f caught", repr(e))

def g(r):
	print("g starting")
	yield
	print("g returning", r)
	return r

f(None)
f(42)
