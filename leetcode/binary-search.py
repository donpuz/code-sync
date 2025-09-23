class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [-1,0,3,5,9,12] target 5
        #       3
        #         5 9 12
        #           9
        #         5
        # we need to calculate mid point from two pointers.
        # if mid point is less than target, set left pointer equal to mid point + 1
        # if mid point is greater than target, set right pointer equal to mid point - 1
        # once i == j on last iter, break. this is the insertion point (or the matching element)
        # return index if the value equals the target. otherwise, return -1
        i = 0
        j = len(nums) - 1

        while i <= j:
            # calculate midpoint

            mid = (j + i) // 2 # there's some optimization here, i don't remember

            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
            # break if after computation, i == j (handled by while loop)

        return -1