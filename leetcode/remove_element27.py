from typing import List


# Counting Sort
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # 1 op
            return 0

        min_value = min(nums)  # N
        counts = [0 for _ in range(min_value, max(nums) + 1)]  # max N

        for v in nums:  # N
            if v != val:
                counts[v - min_value] += 1

        k = 0
        for i in range(len(counts)):  # N
            while counts[i] > 0:
                nums[k] = i + min_value
                counts[i] -= 1
                k += 1

        return k


if __name__ == "__main__":
    nums = [0, 0, 0, 0, 0]
    val = 43
    print(Solution().removeElement(nums, val))
    print(nums)
