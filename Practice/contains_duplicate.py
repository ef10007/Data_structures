import collections
class ContainsDuplicate(object):
    def my_version(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = collections.Counter(nums)
        return True if [value for value in c.values() if value > 1] else False

    def with_set_method(self, nums):
        # print(set(nums))
        return True if len(set(nums)) < len(nums) else False
                
print(ContainsDuplicate().with_set_method([2,14,18,22,22]))
