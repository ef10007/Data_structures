import collections
import string

class firstUniqChar(object):
    def linear_time(self, s):
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    
    def c_function(self, s):
        alphabets = string.ascii_lowercase
        index = [s.index(l) for l in alphabets if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

s = firstUniqChar()
print(s.c_function("leetcode"))