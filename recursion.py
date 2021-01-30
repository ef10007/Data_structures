class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

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

    def reverse_string_mutates_list(self, lst):
        self.lst = lst
        lst.reverse()
    
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
            nxt = current.next
            current.next = previous 
            previous = current 
            current = nxt

        self.head = previous
        print('--- After swapsies ---')
        # print('previous', previous.value)
        print('current', self.head.value)

    def insert_into_tree(self, root, node):
        # Assigning node as a root if it's not exist.
        if root is None:
            root = node

        else:
            # if node value is bigger than root value, it goes to the right.
            if root.value < node.value:
                print('Adding {} to the right node'.format(node.value))
                if root.right is None:
                    root.right = node
                else:
                    self.insert_into_tree(root.right, node)

            # if node value is smaller than root value, it goes to the left.
            else:
                print('Adding {} to the left node'.format(node.value))
                if root.left is None:
                    root.left = node
                else:
                    self.insert_into_tree(root.left, node)
    
    def search_binary_search_tree(self, value):
        """
        Input:    4
                /  \
               2   7
              / \
             1   3
        And the value to search: 2
        
        Output:
                 2     
                / \   
               1   3
        """
        if root: 
            self.search_binary_search_tree(root.left) 
            print(root.value) 
            # inorder(root.right)

s = Solution()

''' Reverse String '''
lst = ['J', 'i', 'n', 'n', 'y']
s.reverse_string_mutates_list(lst)
print(lst)

''' Swap Nodes in Pairs '''
# s.push_to_linked_list(4)
# s.push_to_linked_list(3)
# s.push_to_linked_list(2)
# s.push_to_linked_list(1)
# print(s.print_linked_list())

# After swapsies
# s.swap_nodes_in_pairs()
# print(s.print_linked_list())

# ''' Reverse Linked List '''
# s.push_to_linked_list(5)
# s.push_to_linked_list(4)
# s.push_to_linked_list(3)
# s.push_to_linked_list(2)
# s.push_to_linked_list(1)
# print(s.print_linked_list())

# s.reverse_list()
# print(s.print_linked_list())

# ''' Binary search tree'''
# root = TreeNode(4)
# print('Root value is', root.value)
# s.insert_into_tree(root, TreeNode(2))
# s.insert_into_tree(root, TreeNode(7))
# s.insert_into_tree(root, TreeNode(1))
# s.insert_into_tree(root, TreeNode(3))

# s.search_binary_search_tree(2)