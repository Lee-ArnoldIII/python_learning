class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

a = [12, 5, 19, 26]
target1 = 24

b = [10, 7, 5, 1]
target2 = 11

print(Solution.twoSum(self, a, target1))
