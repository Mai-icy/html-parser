#
#   Test 'value' attribute of StopIteration exception
#

def pex(e):
	print("%s: %s" % (e.__class__.__name__, e))
	print("value =", e.value)

e = StopIteration()
pex(e)
e = StopIteration("spam")
pex(e)
e.value = "eggs"
pex(e)
