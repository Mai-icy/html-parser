#
#   Restaurant model - version 1
#

from simulation import start, hold, now, run

import random
random.seed(12345)

def generate_customers(howmany):
	for i in range(howmany):
		print("Generating a customer at", now())
		start(customer, i)
		yield from hold(random.expovariate(1/5))

def customer(i):
	print("Customer", i, "starting to eat spam")
	yield from hold(random.normalvariate(10, 5))
	print("Customer", i, "finished eating at", now())

start(generate_customers, 5)
run()
