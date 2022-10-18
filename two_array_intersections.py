def intersect(nums1, nums2):
    ans = []
    val = [num for num in nums1 if num in nums2]
    for ls in [[num] * min(nums1.count(num), nums2.count(num)) for num in set(val)]:
        ans += ls
    return ans


print(intersect([4, 4, 9, 5], [9, 4, 9, 8, 4]))
