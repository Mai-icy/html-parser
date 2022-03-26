#
#   Measure overhead of yield-from delegation of next()
#   vs. using a for-loop.
#

from time import time
import gc

def forloop(n):
	for x in direct(n):
		yield x

def yieldfrom(n):
	yield from direct(n)

def direct(n):
	for x in range(n):
		yield x

def test(gen, arg, name = None):
	name = name or gen.__name__
	sum = 0.0
	count = 0
	for i in range(3):
		gc.collect()
		t1 = time()
		for x in gen(arg):
			pass
		t2 = time()
		t = t2 - t1
		sum += t
		count += 1
		print("%10s %10s   %g" % (name, arg, t))
	print()
	return sum / count

gc.disable()
td = test(direct, 1000000)
tf = test(forloop, 1000000)
ty = test(yieldfrom, 1000000)

ohpc = 100 * (ty - td) / (tf - td)
print("Delegation overhead = %.1f%% of for-loop" % ohpc)

