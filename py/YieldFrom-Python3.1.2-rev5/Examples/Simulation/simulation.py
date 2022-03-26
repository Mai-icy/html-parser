#
#   Generator-based discrete event simulation kernel
#

__all__ = ['now', 'run', 'hold', 'wakeup', 'start']

current_time = 0.0

def now():
	return current_time

from heapq import heappush, heappop
event_queue = []

def schedule(process, time):
	heappush(event_queue, (time, process))

current_process = None

def run():
	global current_time, current_process
	while event_queue:
		current_time, current_process = heappop(event_queue)
		try:
			next(current_process)
		except StopIteration:
			pass

def hold(delay):
	schedule(current_process, now() + delay)
	yield

def wakeup(process):
	schedule(process, now())

def start(function, *args, **kwds):
	wakeup(function(*args, **kwds))

def enqueue(queue):
	queue.append(current_process)
