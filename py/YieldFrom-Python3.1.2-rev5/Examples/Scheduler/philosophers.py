from scheduler import *

class Utensil:

  def __init__(self, id):
    self.id = id
    self.available = True
    self.queue = []

  def acquire(self):
    #print "--- acquire", self.id, "avail", self.available
    if not self.available:
      block(self.queue)
      yield
    #print "--- acquired", self.id
    self.available = False

  def release(self):
    #print "--- release", self.id
    self.available = True
    unblock(self.queue)

def philosopher(name, lifetime, think_time, eat_time, left_fork, right_fork):
  for i in range(lifetime):
    for j in range(think_time):
      print(name, "thinking")
      yield
    print(name, "waiting for fork", left_fork.id)
    yield from left_fork.acquire()
    print(name, "acquired fork", left_fork.id)
    print(name, "waiting for fork", right_fork.id)
    yield from right_fork.acquire()
    print(name, "acquired fork", right_fork.id)
    for j in range(eat_time):
      # They're Python philosophers, so they eat spam rather than spaghetti
      print(name, "eating spam")
      yield
    print(name, "releasing forks", left_fork.id, "and", right_fork.id)
    left_fork.release()
    right_fork.release()
  print(name, "leaving the table")

forks = [Utensil(i) for i in range(3)]
schedule(philosopher("Plato", 7, 2, 3, forks[0], forks[1]), "Plato")
schedule(philosopher("Socrates", 8, 3, 1, forks[1], forks[2]), "Socrates")
schedule(philosopher("Euclid", 5, 1, 4, forks[2], forks[0]), "Euclid")
run()
