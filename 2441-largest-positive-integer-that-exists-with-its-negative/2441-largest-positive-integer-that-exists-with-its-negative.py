class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        print(nums)
        for i in nums:
            neg = i*-1
            if neg in nums:
                return i
                break
        else:
            return -1
        