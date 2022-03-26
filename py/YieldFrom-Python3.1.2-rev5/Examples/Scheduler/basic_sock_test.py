from sys import stdin
from scheduler import *

def loop():
  while 1:
    print("Waiting for input")
    block_for_reading(stdin)
    yield
    print("Input is ready")
    line = stdin.readline()
    print("Input was:", repr(line))
    if not line:
      break

schedule(loop())
run2()
