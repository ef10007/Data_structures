class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution():
    def __init__(self):
        self.lst = None
        self.head = None

    def reverse_string(self, lst):
        """
        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        """
        self.lst = lst
        return list(reversed(lst))
    
    def push_to_linked_list(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def print_linked_list(self): 
        temp = self.head 
        while(temp): 
            print(temp.value)
            temp = temp.next

    def swap_nodes_in_pairs(self):
        """
        Input: 1->2->3->4
        Output: 2->1->4->3
        """
        head = self.head

        if head is None: 
            return 

        while (head is not None and head.next is not None): 
            head.value, head.next.value = head.next.value, head.value  
            print('------- head:', self.head.value)
            print('------- next:', self.head.next.value)
            print('------- next.next:', self.head.next.next.value)
            head = head.next.next 

    def reverse_list(self):
        """
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        """

        previous = None
        current = self.head
        print('current', self.head.value)
        
        while (current is not None): 
            print('current in while loop', current.value)
            nt = current.next
            current.next = previous 
            previous = current 
            current = nt

        self.head = previous
        print('--- After swapsies ---')
        # print('previous', previous.value)
        print('current', self.head.value)
        

s = Solution()

''' Reverse String '''
lst = ['J', 'i', 'n', 'n', 'y']
# rev = s.reverse_string(lst)
# print(rev)

''' Swap Nodes in Pairs '''
# s.push_to_linked_list(4)
# s.push_to_linked_list(3)
# s.push_to_linked_list(2)
# s.push_to_linked_list(1)
# print(s.print_linked_list())

# After swapsies
# s.swap_nodes_in_pairs()
# print(s.print_linked_list())

''' Reverse Linked List '''
# s.push_to_linked_list(5)
# s.push_to_linked_list(4)
# s.push_to_linked_list(3)
# s.push_to_linked_list(2)
# s.push_to_linked_list(1)
# print(s.print_linked_list())

# s.reverse_list()
# print(s.print_linked_list())
