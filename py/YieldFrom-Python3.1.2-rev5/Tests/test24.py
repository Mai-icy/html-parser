#
#   Test parser module
#

import parser

def test(src):
	st1 = parser.suite(src)
	tup1 = st1.totuple()
	print(tup1)
	st2 = parser.sequence2st(tup1)
	tup2 = st2.totuple()
	print(tup1 == tup2)

test("yield from 1")
test("f(yield from 1)")
