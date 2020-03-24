class InputOutput:
    def __init__(self, word):
        self.word = word

    '''1. A Python instruction which would output a blank line.'''
    # print("Please key in a word: ")
    # print("")

    '''2. an instruction which would output
        Hickory, Dickory, Dock'''
    # print("Please type 'Hickory, Dickory, Dock': ")
    # word = input()

    '''3. a program which reads in two words, one after the other, and then displays them in reverse order.'''
    print("Please key in a word: ", end='')
    word1, word2 = input().split(',')
    print("The reverse-order will be ", end='')
    print(word2, word1)