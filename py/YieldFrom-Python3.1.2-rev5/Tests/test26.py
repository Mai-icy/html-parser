#
#   Test throwing GeneratorExit into a subgenerator that
#   catches it and returns normally.
#

def f():
	try:
		print("Enter f")
		yield
		print("Exit f")
	except GeneratorExit:
		return

def g():
	print("Enter g")
	yield from f()
	print("Exit g")

gi = g()
next(gi)
gi.throw(GeneratorExit)
