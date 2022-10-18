# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def two_sum(nums, target):
    hash_map = {v: i for i, v in enumerate(nums)}
    for i in range(len(nums)):
        other_index = hash_map.get(target - nums[i])
        if other_index is not None and other_index != i:
            return [i, hash_map.get(target - nums[i])]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))  # Should return [1, 2]
