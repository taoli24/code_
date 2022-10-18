# Given an array, rotate the array to the right by k steps, where k is non-negative.
from typing import List


def rotate(nums: List[int], k: int) -> None:
    l = len(nums)
    for i in range(l-k):
        temp = nums[i + k]
        nums[(i + 2 * k) % l] = temp
        nums[(i + k) % l] = nums[i]
    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)  # Should arrange array into [5,6,7,1,2,3,4]
