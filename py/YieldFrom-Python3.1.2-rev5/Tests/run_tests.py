#
#   Run all the yield-from tests
#

import os, sys, traceback
from glob import glob

actdir = "actual"
expdir = "expected"

def compile_file(path):
	source = open(path, "rU").read()
	return compile(source, path, 'exec')

def number(name):
	return int(name[4:-3])

def compare(name):
	actpath = os.path.join(actdir, name + ".out")
	exppath = os.path.join(expdir, name + ".out")
	if not os.path.exists(exppath):
		print("%s is missing" % exppath)
		return False
	if open(actpath).read() == open(exppath).read():
		return True
	else:
		os.system("diff -u %s %s" % (exppath, actpath))
		return False

def run_test(name):
	outdir = actdir
	outpath = os.path.join(outdir, name + ".out")
	out = open(outpath, "w")
	try:
		sys.stdout = sys.stderr = out
		try:
			exec(compile_file(name), {})
		except:
			et, ev, tb = sys.exc_info()
			tb = tb.tb_next
			traceback.print_exception(et, ev, tb)
	finally:
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__
		out.close()
	return compare(name)

def main():
	total = 0
	failures = []
	names = glob("test*.py")
	names.sort(key = number)
	for name in names:
		total += 1
		print(name)
		if not run_test(name):
			failures.append(name)
	print("Passed:", total - len(failures), "of", total)
	if not failures:
		print("All tests OK.")
	else:
		print("FAILED:", " ".join(failures))

main()
