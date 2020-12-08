class TwoSum(object):
    # nums: List[int], target: int, return type: List[int]
    def brute_force(self, nums, target):
        """
        Time complexity : O(n^2)
        Space complexity : O(1)
        """
        for i in nums:
            for j in nums:
                if j == target - i:
                    return [i, j]
                break

    def two_pass_hash_table(self, nums, target):
        """
        A hash table trades space for speed.
        Time complexity : O(n)
        Space complexity : O(n)
        """
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[i] = num
        for i, num in enumerate(nums):
            complement = target - num 
            if (complement in hashmap) and (complement != num):
                return [complement, num]

    def one_pass_hash_table(self, nums, target):
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[i] = num
            complement = target - num
            if complement in hashmap.values():
                return [complement, num]
            
# s = TwoSum()
# a1 = s.brute_force([2,7,11,15], 9)
# print(a1)
# a2 = s.two_pass_hash_table([2,7,11,15], 9)
# print(a2)
# a3 = s.one_pass_hash_table([2,7,11,15], 9)
# print(a3)



