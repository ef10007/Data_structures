class moveZeroesInPlace(object):
    def pop_n_append(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums))[::-1]:
            print(i, nums[i])
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        print(nums)

        # for i in range(len(nums)):
        #     print(i, nums[i])
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        # print(nums)

c = moveZeroesInPlace()
c.pop_n_append([0,1,0,3,12])