import math as m

class IsPowerOfThree(object):
    def while_loop(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:       	
        	n /= 3
        return True if n == 1.0 else False

    def math_module(self, n):
        return (m.log10(n) / m.log10(3)) % 1 == 0
 
i = IsPowerOfThree()
print(i.math_module(9))
