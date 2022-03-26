#
#   Test catching an exception thrown into a
#   subgenerator and returning a value
#

def inner():
   try:
       yield 1
   except ValueError:
       print("inner caught ValueError") #pass
   return 2

def outer():
   v = yield from inner()
   print("inner returned %r to outer" % v)
   yield v

g = outer()
print(next(g))              # prints 1
print(g.throw(ValueError))  # prints 2
