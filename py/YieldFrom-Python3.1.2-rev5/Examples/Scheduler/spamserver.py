from socket import *
from scheduler import *

port = 4200

class BadRequest(Exception):
  pass

def sock_accept(sock):
  block_for_reading(sock)
  yield
  return sock.accept()

def sock_readline(sock):
  buf = b""
  while buf[-1:] != b"\n":
    block_for_reading(sock)
    yield
    data = sock.recv(1024)
    if not data:
      break
    buf += data
  if not buf:
    close_fd(sock)
  return buf

def sock_write(sock, data):
  while data:
    block_for_writing(sock)
    yield
    n = sock.send(data)
    data = data[n:]

def listener():
  lsock = socket(AF_INET, SOCK_STREAM)
  lsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  lsock.bind(("", port))
  lsock.listen(5)
  while 1:
    csock, addr = yield from sock_accept(lsock)
    print("Listener: Accepted connection from", addr)
    schedule(handler(csock))

def handler(sock):
  while 1:
    line = yield from sock_readline(sock)
    if not line:
      break
    try:
      n = parse_request(line)
      yield from sock_write(sock, b"100 SPAM FOLLOWS\n")
      for i in range(n):
        yield from sock_write(sock, b"spam glorious spam\n")
    except BadRequest:
      yield from sock_write(sock, b"400 WE ONLY SERVE SPAM\n")

def parse_request(line):
  tokens = line.split()
  if len(tokens) != 2 or tokens[0] != b"SPAM":
    raise BadRequest
  try:
    n = int(tokens[1])
  except ValueError:
    raise BadRequest
  if n < 1:
    raise BadRequest
  return n

schedule(listener())
run2()
