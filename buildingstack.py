def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1: # The first while loop represents the recursive calls lead to a base case
    execution_context = {"n_value": n}
    call_stack.append(execution_context) # adding context to the end of call_stack list (= being pushed onto the call stack)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED") # print when n == 1
  
  while len(call_stack) != 0: # The second loop will run as long as there are execution contexts stored in call_stack list
    return_value = call_stack.pop() # .pop() function prevents an infinite loop
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  print("The final result is", result)
  return result, call_stack

sum_to_one(4)
# [{'n_value': 4}]
# [{'n_value': 4}, {'n_value': 3}]
# [{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
# BASE CASE REACHED
# Return value of 2 adding to result 1
# Return value of 3 adding to result 3
# Return value of 4 adding to result 6
# The final result is 10
