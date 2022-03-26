#
#   Test returning value from delegated 'throw'
#

def g1():
	try:
		print("Starting g1")
		yield "g1 ham"
		yield from g2()
		yield "g1 eggs"
	finally:
		print("Finishing g1")

def g2():
	try:
		print("Starting g2")
		yield "g2 spam"
		yield "g2 more spam"
	except LunchError:
		print("Caught LunchError in g2")
		yield "g2 lunch saved"
		yield "g2 yet more spam"

class LunchError(Exception):
	pass

g = g1()
for i in range(2):
	x = next(g)
	print("Yielded", x)
e = LunchError("tomato ejected")
g.throw(e)
for x in g:
	print("Yielded", x)
