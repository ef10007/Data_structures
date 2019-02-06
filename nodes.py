
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
  
  def set_link_node(self, link_node):
    self.link_node = link_node
    
blueberry = Node("blue")
strawberry = Node("red")
raspberry = Node("also red")

raspberry.set_link_node(strawberry)
blueberry.set_link_node(raspberry)

rasps_data = blueberry.get_link_node().get_value()
straws_data = raspberry.get_link_node().get_value()

blues_data = blueberry.get_value()

print(rasps_data) # also red
print(straws_data) # red
print(blues_data) # blue
