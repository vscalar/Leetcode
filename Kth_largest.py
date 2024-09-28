class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def Merge(left: List[int], right: List[int]):
            if left[0] >= right[0]:
                return left + right
            
            else:
                return right + left

        def MergeSort(nums: List[int]):
            length = len(nums)
            if length <= 1:
                return nums
            
            left = mergeSort(nums[0:n/2])
            right = metgeSort(nums[n/2:n])

            return Merge(left, right)

        if len(nums) <= 50:
            sortedNums = MergeSort(nums)
            print(sortedNums[k-1])
            