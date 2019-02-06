from nodes import Node
# With stacks, size matters.

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.limit = limit
    self.size = 0
    
  def push(self, value):
    if self.has_space() == True:
      
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("The stack is already full")

  def pop(self):
    
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1 #stack size's decreased by 1
      return item_to_remove.get_value()
    else:
      print("This stack is empty.")
      break
    
  def peek(self):
    
    if not self.is_empty():
      return self.top_item.get_value()
    else:
      print("Nothing to peek.")
      
  def has_space(self):
    if self.limit > self.size:
      return True
    
  def is_empty(self):
    if self.size == 0:
      return True

      
      
