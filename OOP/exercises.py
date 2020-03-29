class InputOutput:
    def __init__(self, word=''):
        self.word = word
    
    def inputting(self):
        word = input()
        return word
    
    def outputting_in_reverse(self):
        print("Please key in two words separated by comma: ", end='')
        lst = []
        word1, word2 = self.inputting().split(',')
        lst.append((word1, word2))
        lst.reverse()
        return lst[0]

    def string_concatenation(self):
        print("Please key in a word: ", end='')
        word1 = self.inputting()
        print("And now key in another: ", end='')
        word2 = self.inputting()
        print(f'You have typed: {word1} and {word2}.')


    def string_comparison(self, first_word, second_word):
        if first_word > second_word == True:
            print('{} comes before {}'.format(first_word, second_word))
        else:
            print('{} comes before {}'.format(second_word, first_word))

    def arithmetical_process(self, dividend, divisor):
        if dividend + divisor > 100:
            print('It exceeds 100')
            return
        if divisor == 0:
            print('Cannot divide by zero')
            return
        quotient = round(dividend / divisor)
        remainder = dividend % divisor
        if remainder == 0:
            print(f'The result is {quotient} without a remainder')
        else:
            print(f'The result is {quotient} with a remainder of {remainder}')

    def greeting_clock(self, num):
        if num > 2400 or num < 0:
            print('Wrong input')
        elif num > 600 and num < 960:
            print('Morning')  
        elif num > 1200 and num < 1360:
            print('Afternoon')
        elif num > 1900 and num < 2060:
            print('Evening')
        else:
            print('Stay calm keep coding')

    def squares(self):
        num = 1
        sqnum = 0
        while sqnum < 100:
            sqnum = num ** 2
            print(sqnum)
            num += 1
            
    def max_and_min(self):
        print("Please type five numbers separated by comma: ")
        lst = []
        num1, num2, num3, num4, num5 = self.inputting().split(',')
        lst.append([num1, num2, num3, num4, num5])
        return int(max(lst[0])), int(min(lst[0]))

    def booleans(self, condition):
        if condition == True:
            print('True')
        else: 
            print('False')
        
    def series_of_nums(self):
        total = 0
        count = 0 
        finished = False
        while not finished:
            print("Please enter a number (end with 0):")
            s = input()
            num = int(s)
            if num != 0:
                total += 1
            elif num == 10:
                count +=1
            else:
                finished = True
        print(f'You have entered {total} numbers and 10 {count} times. ')

 
if __name__ == "__main__":
    i = InputOutput()
    # ip = i.inputting()
    # print(ip)
    # oir = i.outputting_in_reverse()
    # print(oir)
    # i.string_concatenation()

    # i.string_comparison("A", "9")
    # i.string_comparison("Zurich", "acapulco")
    # i.string_comparison("Abba", "ABBA")
    # i.string_comparison("long_thing_with_a_$", "long_thing_with_a_&")
    # i.string_comparison("King@example.invalid", "King Kong")

    # i.arithmetical_process(10,2)
    # i.greeting_clock(-964)
    # i.squares()
    # r = i.max_and_min()
    # print(r)

    # x = 5
    # y = 20
    # s = 'Birkbeck'
    # i.booleans(x == 5 and y == 10)
    # i.booleans(x < 0 or y > 15)
    # i.booleans(y % x == 0 and len(s) == 8)
    # i.booleans(s[1:3] == "Bir" or x // y > 0)

    i.series_of_nums()

