class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # -6 2 3 7 8 15 target 9
        # -10 -1 0 target -1
        # 2 pointers
        # add up two pointers. if greater than target, move right pointer
        # if less than target, move left pointer

        i = 0
        j = len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else: # equal
                return [i+1, j+1]