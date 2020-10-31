# Write a Python program that first lets the user enter one string. Your program should then print a string in which the occurrences of "x" in the user's input have been replaced by "o" and the occurrences of "o" have been replaced by "x". All other letters should be unchanged.

# For example, if the user enters "Box oxymoron", your program should print:
# foo = somevalue
# previous = next_ = None
# l = len(objects)
# for index, obj in enumerate(objects):
#     if obj == foo:
#         if index > 0:
#             previous = objects[index - 1]
#         if index < (l - 1):
#             next_ = objects[index + 1]

def up_n_down():
    upcount = 0 
    samecount = 0
    downcount = 0
    print("Please enter a number (end with 0):", end='')
    n = input()
    curr = int(n)
    print("Enter the next number (0 to finish):", end='')
    n2 = input()
    nxt = int(n2)
    while nxt != 0:
        print("Enter the next number (0 to finish):", end='')
        n2 = input()
        nxt = int(n2)
        if curr > nxt:
            upcount += 1
        elif curr == nxt:
            samecount +=1
        elif curr < nxt:
            downcount +=1
        else:
            curr = 0
            nxt = 0
        break
    print(f' Up: {upcount} \n Same: {samecount} \n Down: {downcount}')
# up_n_down()

def crash(dltr):
    result=0
    temp=1
    for i in range(1, dltr):
        temp = temp * i
        for k in range(i):
            result += temp
    return result
# print(crash(4))


def y(x):
    global a
    a = 4
    return 0

def f(a):
    a = 3
    print(a)
    return a
# a = 5
# f(a)
# print(a)
# y(a)
# print(a)

# arr = [1.4,3.7,4.8,6.3,99.9] 
# x = arr.pop(2)
# print(x)
# print(arr)

import numpy as np
print(np.transpose(np.array([[1, 2, 3], [4, 5, 6]])))