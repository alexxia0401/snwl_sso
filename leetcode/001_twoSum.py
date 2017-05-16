#!/usr/bin/python3

# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i, value in enumerate(nums):
            if value not in temp:
                temp[target-value] = i
            else:
                return [temp[value], i]

if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6

    sln = Solution().twoSum(nums, target)
    print(sln)
