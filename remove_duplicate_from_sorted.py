# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

# [0,0,1,1,1,2,2,3] -> [0,1,2,3]

# remove with two pointers
# def remove_duplicate(nums):
#     i, k = 0, 0
#     while i < len(nums) and k < len(nums):
#         j = i + 1
#         nums[k] = nums[i]
#         while j < len(nums):
#             if nums[i] == nums[j]:
#                 j += 1
#             else:
#                 i = j
#                 break
#         if nums[k] == nums[len(nums)-1]:
#             break
#         k += 1
#     return k + 1

def remove_duplicate(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            # found unique
            nums[k] = nums[i]
            k += 1
    return k


print(remove_duplicate([1, 1, 2]))
