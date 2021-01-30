class FizzBuzz:
    def my_version(self, n):
        lst = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                i = 'FizzBuzz'
                lst.append(i)
            elif i % 3 == 0:
                i = 'Fizz'
                lst.append(i)
            elif i % 5 == 0:
                i = 'Buzz'
                lst.append(i)
            else:
                lst.append(i)
        return [str(i) for i in lst]
    
    def naive_approach(self, n):
        ans = []
        for num in range(1, n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans

    def fizz_buzz_jazz(self, n):
        ans = []
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            divisible_by_7 = (num % 7 == 0)
            string = ''

            if divisible_by_3:
                string += "Fizz"
            if divisible_by_5:
                string += "Buzz"
            if divisible_by_7: 
                string += "Jazz" 
            if not string:
                string = str(num)
            ans.append(string)
        return ans



f = FizzBuzz()
answer = f.fizz_buzz_jazz(30)
print(answer)