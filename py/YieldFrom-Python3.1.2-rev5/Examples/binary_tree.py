#
#   Here is a binary tree that produces an inorder traversal
#   of its items when iterated over. (Courtesy of Scott Dial)
#

class BinaryTree:
  def __init__(self, left=None, us=None, right=None):
    self.left = left
    self.us = us
    self.right = right

  def __iter__(self):
    if self.left:
      yield from self.left
    if self.us:
      yield self.us
    if self.right:
      yield from self.right

#
#   For comparison, here is the same thing using for-loops
#   instead of yield-from.
#

class BinaryTree_ForLoop:
  def __init__(self, left=None, us=None, right=None):
    self.left = left
    self.us = us
    self.right = right

  def __iter__(self):
    if self.left:
      for node in self.left:
        yield node
    if self.us:
      yield self.us
    if self.right:
      for node in self.right:
        yield node
