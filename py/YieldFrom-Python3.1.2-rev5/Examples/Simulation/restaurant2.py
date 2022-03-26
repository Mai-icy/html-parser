#
#   Restaurant model - version 2
#

from simulation import start, hold, now, run
from resource import Resource

import random
random.seed(12345)

def generate_customers(howmany):
	for i in range(howmany):
		print("Generating a customer at", now())
		start(customer, i)
		yield from hold(random.expovariate(1/5))

tables = Resource(3)
waiters = Resource(1)

def customer(i):
	print("Customer", i, "arriving at", now())
	yield from tables.acquire(1)
	print("Customer", i, "sits down at a table at", now())
	yield from waiters.acquire(1)
	print("Customer", i, "orders spam at", now())
	yield from hold(random.normalvariate(20, 2))
	waiters.release(1)
	print("Customer", i, "gets served spam at", now())
	yield from hold(random.normalvariate(10, 5))
	print("Customer", i, "finished eating at", now())
	tables.release(1)

start(generate_customers, 5)
run()
