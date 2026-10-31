"""The main challenge here was not finding the maximum.
It was lowering the memory usage as much as possible by dequeuing useless data"""
# (ALGO) if: data before current max. Then: data is useless. Otherwise: keep it
# Leetcode Challenge: Max Sliding Window
# Github: KhalidsCS   :)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        dq = deque([])

        for i in range(0, min(len(nums), k)):
            while dq and nums[i] > dq[-1][1]:
                dq.pop()
            dq.append((i, nums[i]))

        max_list.append(dq[0])

        for i in range(k, len(nums)):
            if dq[0][0] < i - k + 1:
                dq.popleft()
            while dq and nums[i] > dq[-1][1]:
                dq.pop()
            dq.append((i, nums[i]))
            max_list.append(dq[0])
        return [i[1] for i in max_list]
