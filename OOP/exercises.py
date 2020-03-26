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
        print('You have typed:', word1 + ' ' + word2)

    def string_comparison(self, first_word, second_word):
        if first_word > second_word == True:
            print('{} comes before {}'.format(first_word, second_word))
        else:
            print('{} comes before {}'.format(second_word, first_word))

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
