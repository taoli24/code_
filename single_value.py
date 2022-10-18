from collections import Counter


def single_value(nums):
    count = Counter(nums)
    for k, v in count.items():
        if v == 1:
            return k


print(single_value([4, 4, 3, 1, 2, 1, 2]))
