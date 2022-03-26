#
#   Discrete event simulation - Resources
#

from simulation import enqueue, wakeup

class Resource:

	def __init__(self, capacity):
		self.available = capacity
		self.queue = []
	
	def acquire(self, amount):
		enqueue(self.queue)
		if len(self.queue) > 1:
			yield
		while amount > self.available:
			yield
		self.queue.pop(0)
		self.available -= amount
	
	def release(self, amount):
		self.available += amount
		if self.queue:
			wakeup(self.queue[0])
