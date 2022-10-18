# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


def plusOne(digits):
    l = len(digits)
    reverse_digits = digits[::-1]
    reverse_digits[0] += 1
    for i in range(l):
        if reverse_digits[i] == 10:
            reverse_digits[i] = 0
            if i != l-1:
                reverse_digits[i + 1] += 1
            else:
                reverse_digits.append(1)
    return reverse_digits[::-1]


print(plusOne([4, 3, 2, 9]))
print(plusOne([9]))
