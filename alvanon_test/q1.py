# Rearrange an array of integers so that the calculated value U is maximized. Among the
# arrangements that satisfy that test, choose the array with minimal ordering. The value of U
# for an array with n elements is calculated as :
# U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×arr[n-1] × (1÷arr[n]) if n is odd
# or
# U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×(1÷arr[n-1]) × arr[n] if n is even
# The sequence of operations is the same in either case, but the length of the array, n,
# determines whether the calculation ends on arr[n] or (1÷arr[n]).
# Arrange the elements to maximize U and the items are in the numerically smallest possible
# order.

from functools import reduce
import math
from typing import List, Tuple


class Solution:
    def has_non_integer_element(self, arr: List[int]) -> bool:
        for item in arr:
            if not isinstance(item, int):
                return True
        return False

    def calculate_maximum_u(self, nums: List[int]) -> Tuple[List[int], float]:
        if not nums or nums == []:
            return nums, None
        if 0 in nums:
            return nums, 0
        if self.has_non_integer_element(nums):
            return nums, None
        positive = reduce(lambda x, y: x * y, nums)
        if positive > 0:
            nums.sort(key=lambda x: math.fabs(x))
        else:
            nums.sort(key=lambda x: math.fabs(x), reverse=True)
        n = len(nums)
        count = 0
        res_v = []
        res_r = []
        last_item = None
        while nums:
            if count == n - 1 and n % 2 == 0:
                last_item = nums.pop(-1)
                res_v.append(last_item)
            elif count == n - 1 and n % 2 == 1:
                last_item = nums.pop(-1)
                res_r.append(last_item)
            elif count % 3 != 2:
                res_v.append(nums.pop(-1))
            else:
                res_r.append(nums.pop(0))
            count += 1
        res = []
        u = 1
        res_v.sort()
        res_r.sort()
        print(res_v, res_r)
        for i in range(n):
            if i == n - 1:
                if res_v:
                    item = res_v.pop(0)
                    res.append(item)
                    u *= item
                else:
                    item = res_r.pop(0)
                    res.append(item)
                    u /= item
            elif i % 3 != 2:
                item = res_v.pop(0)
                res.append(item)
                u *= item
            else:
                item = res_r.pop(0)
                res.append(item)
                u /= item
        return res, u


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    res = s.calculate_maximum_u(nums)
    print(res)
