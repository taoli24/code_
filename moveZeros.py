# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeros(nums):
    zero_counts = 0
    i = 0
    while i < len(nums):
        try:
            if nums[i] == 0:
                nums.pop(i)
                zero_counts += 1
                i -= 1
        except IndexError:
            break
        i += 1
    nums += [0] * zero_counts
    print(nums)
    return nums + [0] * zero_counts


print(moveZeros([0, 1, 0, 3, 12]))
print(moveZeros([0, 0, 1]))
