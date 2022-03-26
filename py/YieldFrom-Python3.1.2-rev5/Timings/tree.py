#
#   Measure time taken to traverse a tree recursively
#   using a generator.
#

from time import time
import gc

def build_tree(n):
	if not n:
		return 1
	else:
		return (build_tree(n-1), build_tree(n-1))

#print build_tree(4)

def forloop(node):
	if node == 1:
		yield node
	else:
		for x in forloop(node[0]):
			yield x
		for x in forloop(node[1]):
			yield x

def yieldfrom(node):
	if node == 1:
		yield node
	else:
		yield from yieldfrom(node[0])
		yield from yieldfrom(node[1])

def time_case(gen, tree, arg):
	name = gen.__name__
	sum = 0.0
	count = 0
	for i in range(3):
		gc.collect()
		#print "GC:", gc.get_count()
		t1 = time()
		for x in gen(tree):
			pass
		t2 = time()
		t = t2 - t1
		print("%10s %10s   %g" % (name, arg, t))
		sum += t
		count += 1
	print()
	return sum / count

def do_case(results, n):
	tree = build_tree(n)
	tf = time_case(forloop, tree, n)
	ty = time_case(yieldfrom, tree, n)
	results.append((n, tf, ty))

gc.disable()
results = []
nc = 20
for n in range(1, nc + 1):
	do_case(results, n)
for (i, tf, ty) in results:
	print("%3d %f %f %g" % (i, tf, ty, tf / ty))
