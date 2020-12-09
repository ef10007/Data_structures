class ValidParentheses(object):
    def stacks(self, s):
        stack = []
        mapping = {')':'(', ']': '[', '}':'{'}

        for char in s:
            if char in mapping: # keys = closing bracket
                stack.pop() if stack else "empty"
            else: # values = opening bracket
                stack.append(char)
        
        if len(stack) > 0:
            return "Invalid expression"
        else:
            return "Valid"
        
s = ValidParentheses()
a = s.stacks('()')
print(a)