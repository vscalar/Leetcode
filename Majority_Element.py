class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = dict()
        threshold = len(nums) // 2
        for number in nums:
            try:
                tmp = d[number]
                d[number] = tmp + 1
            
            except:
                d[number] = 1

            if d[number] > threshold:
                return number