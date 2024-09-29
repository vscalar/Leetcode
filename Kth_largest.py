class Solution:
    import sys
    sys.setrecursionlimit(10**6)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def Merge(left: tuple, right: tuple) -> list[int]:
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        def MergeSort(nums: list[int]) -> list[int]:
            n = len(nums)
            if n <= 1:
                return nums
            
            left = MergeSort(tuple(nums[0:n//2]))
            right = MergeSort(tuple(nums[n//2:n]))

            return Merge(left, right)
        
        #get random value between left and right
        def GetPivot(left: int, right: int) -> int:
            import random
            return random.randint(left, right)
            
        #modify nums to [bigger]+[pivot]+[smaller], return a index where pivot exists
        def Partition(left: int, right: int, pivot: int) -> tuple:
            pivotVal = nums[pivot]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            store_index = left
            occurence = 0
            
            for i in range(left, right):
                if nums[i] >= pivotVal:  
                    if nums[i] == pivotVal: occurence += 1
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index, occurence
            
        def GetKth(left: int, right: int, k: int) -> int:
            if left == right:
                return nums[left]
            
            if len(nums) <= 50:
                sortedNums = MergeSort(nums)
                return sortedNums[k]
            
            pivotIndex = GetPivot(left, right)
            pivotIndex, occurence = Partition(left, right, pivotIndex)

            
            if k == pivotIndex:
                return nums[k]
            #search for bigger part
            elif k < pivotIndex: 
                if occurence > pivotIndex - k + 1: return nums[k]
                return GetKth(left, pivotIndex - 1, k)
            #search for smaller part
            else:
                return GetKth(pivotIndex + 1, right, k) 
    
        return GetKth(0, len(nums) - 1, k-1)