#---------------------------------------------------------------------
#
#   Simple generator-based thread scheduler
#
#---------------------------------------------------------------------

__all__ = ['run', 'schedule', 'unschedule', 'block', 'unblock',
           'run2', 'block_for_reading', 'block_for_writing', 'close_fd']

current = None
ready_list = []
names = {}

def names_of(seq):
  return "[%s]" % ", ".join([names.get(g) for g in seq])

#
#   Basic scheduling, no outside events
#

def schedule(g, name = None):
  if name:
    names[g] = name
  ready_list.append(g)

def unschedule(g):
  if g in ready_list:
    ready_list.remove(g)

def block(queue):
  queue.append(current)
  unschedule(current)
  #print "--- blocked", names_of(queue)

def unblock(queue):
  if queue:
    g = queue.pop(0)
    schedule(g)
    #print "--- unblock", names_of(queue)

def expire_timeslice(g):
  if ready_list and ready_list[0] is g:
    del ready_list[0]
    ready_list.append(g)

def run():
  global current
  while ready_list:
    #print "--- ready", names_of(ready_list)
    g = ready_list[0]
    current = g
    try:
      next(g)
    except StopIteration:
      unschedule(g)
    else:
      expire_timeslice(g)
      
#
#   Scheduling with select() on files
#

class FdQueues:

  def __init__(self):
    self.readq = []
    self.writeq = []

fd_queues = {} # fd -> FdQueues

def get_fd_queues(fd):
  q = fd_queues.get(fd)
  if not q:
    q = FdQueues()
    fd_queues[fd] = q
  return q

def block_for_reading(fd):
  block(get_fd_queues(fd).readq)

def block_for_writing(fd):
  block(get_fd_queues(fd).writeq)

def close_fd(fd):
  if fd in fd_queues:
    del fd_queues[fd]
  fd.close()

def wait_for_event():
  from select import select
  read_fds = []
  write_fds = []
  for fd, q in fd_queues.items():
    if q.readq:
      read_fds.append(fd)
    if q.writeq:
      write_fds.append(fd)
  if not (read_fds or write_fds):
    return False
  read_fds, write_fds, _ = select(read_fds, write_fds, [])
  for fd in read_fds:
    unblock(fd_queues[fd].readq)
  for fd in write_fds:
    unblock(fd_queues[fd].writeq)
  return True

def run2():
  while 1:
    run()
    if not wait_for_event():
      return
