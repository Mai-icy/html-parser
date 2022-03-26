#
#   Test raising exception in initial next() call
#

def g1():
	try:
		print("Starting g1")
		yield from g2()
	finally:
		print("Finishing g1")

def g2():
	try:
		print("Starting g2")
		raise ValueError("spanish inquisition occurred")
	finally:
		print("Finishing g2")

for x in g1():
	print("Yielded", x)
