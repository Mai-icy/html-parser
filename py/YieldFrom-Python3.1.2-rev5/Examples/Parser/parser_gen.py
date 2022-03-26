import re, sys
pat = re.compile(r"(\S+)|(<[^>]*>)")

text = "<foo> This is a <b> foo file </b> you know. </foo>"

def run():
  parser = parse_items()
  next(parser)
  try:
    for m in pat.finditer(text):
      token = m.group(0)
      print("Feeding:", repr(token))
      parser.send(token)
    parser.send(None) # to signal EOF
  except StopIteration as e:
    tree = e.value
    print(tree)

def parse_elem(opening_tag):
  name = opening_tag[1:-1]
  closing_tag = "</%s>" % name
  items = yield from parse_items(closing_tag)
  return (name, items)

def parse_items(closing_tag = None):
  elems = []
  while 1:
    token = yield
    if not token:
      break # EOF
    if is_opening_tag(token):
      elems.append(yield from parse_elem(token))
    elif token == closing_tag:
      break
    else:
      elems.append(token)
  return elems

def is_opening_tag(token):
  return token.startswith("<") and not token.startswith("</")

run()
