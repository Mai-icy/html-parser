#
#   Test parsing yield from as function argument
#

from dis import dis

def g():
	f(yield from x)

dis(g)
