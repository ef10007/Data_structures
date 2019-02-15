class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1
  
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  # END OF HEAP HELPER METHODS

  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
  	
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    
    self.heap_list[1] = self.heap_list[self.count] # swapping element at index 1 with the last element(count) in heap_list
    self.heap_list.pop() # removing the last element from the heap_list
    self.count -= 1 # decrementing the count by 1
    
    print("Last element moved to first: {0}".format(self.heap_list))
    self.heapify_down()
    return min
  
  def heapify_down(self):
      print("Heapifying down!")
      idx = 1
    
  def add(self, element):
    self.count += 1 # incrementing the element count in heap_list
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  def get_smaller_child_idx(self, idx):
    
    if self.right_child_idx(idx) > self.count: # there's no right child for this idx
      print("There is only a left child/ no right child")
      return self.left_child_idx(idx)
    
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      
      if left_child < right_child:
        print("Left child is smaller")
        return self.left_child_idx(idx)
      else:
        print("Right child is smaller")
        return self.right_child_idx(idx)
  
    
  def heapify_up(self):
    print("Heapifying up")
    idx = self.count # retrieving the last index of heap_list
    
    while self.parent_idx(idx) > 0: # valid parent index is greater than 0
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      
      if parent > child:
        print("swapping {0} with {1}".format(parent, child))
        
        parent = self.heap_list[idx]
        child = self.heap_list[self.parent_idx(idx)]
      
#       if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        
#         tmp = self.heap_list[self.parent_idx(idx)]
#         print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
#         self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
#         self.heap_list[idx] = tmp
        
      idx = self.parent_idx(idx) # setting idx to be the index of its parent
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("") 
    
    element_count = len(self.heap_list)
    if element_count > 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")
      
    
    def heapify_down(self):
      idx = 1
      # starts at 1 because we swapped first and last elements
      swap_count = 1
      
      while self.child_present(idx): # while idx has a child element
        smaller_child_idx = self.get_smaller_child_idx(idx)
        if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
          swap_count += 1
          tmp = self.heap_list[smaller_child_idx]
          self.heap_list[smaller_child_idx] = self.heap_list[idx]
          self.heap_list[idx] = tmp
        idx = smaller_child_idx

      element_count = len(self.heap_list)
      if element_count >= 10000:
        print("Heap of {0} elements restored with {1} swaps"
              .format(element_count, swap_count))
        print("")  

    
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  min_heap.add(el)


# test it out, is the minimum number at index 1?
print(min_heap.heap_list)


# add elements
min_heap.add(7)
min_heap.add(12)
min_heap.add(42)

# remove minimum element
print(min_heap.retrieve_min())

# populate min_heap with descending numbers
descending_nums = [n for n in range(10001, 1, -1)]
print("ADDING!")
for el in descending_nums:
  min_heap.add(el)
#ADDING!
#Heap of 10001 elements restored with 13 swaps  
  

print("REMOVING!")
# remove minimum until min_heap is empty
min_heap.retrieve_min()
#REMOVING!
#Heap of 10000 elements restored with 13 swaps

