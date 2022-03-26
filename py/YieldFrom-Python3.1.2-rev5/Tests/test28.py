#
#   Test throwing GeneratorExit into a subgenerator that
#   catches it and raises a different exception.
#

def f():
	try:
		print("Enter f")
		yield
		print("Exit f")
	except GeneratorExit:
		raise ValueError("Vorpal bunny encountered")

def g():
	print("Enter g")
	yield from f()
	print("Exit g")

gi = g()
next(gi)
gi.throw(GeneratorExit)
