import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = collections.Counter(s) 
        tt = collections.Counter(t) 
        
        return True if ss == tt else False

print(Solution().isAnagram("anagram", "nagaram"))
