#
#   Test generator return value
#

def g1():
	print("Starting g1")
	yield "g1 ham"
	ret = yield from g2()
	print("g2 returned", ret)
	ret = yield from g2(42)
	print("g2 returned", ret)
	yield "g1 eggs"
	print("Finishing g1")

def g2(v = None):
	print("Starting g2")
	yield "g2 spam"
	yield "g2 more spam"
	print("Finishing g2")
	if v:
		return v

for x in g1():
	print("Yielded", x)
