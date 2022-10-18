def reverse_integer(num):
    if num == 0:
        return 0

    num = [i for i in str(num)]
    # Remove tail zeros
    while True:
        r = -1
        if num[r] == '0':
            num.pop()
        else:
            break

    rv = int(''.join(num[::-1]) if num[0] != '-' else '-'+''.join(num[::-1][:-1]))

    return rv if (2 ** 31) - 1 > rv > -2 ** 31 else 0


print(reverse_integer(-123))
print(reverse_integer(1200))
print(reverse_integer(0))
print(reverse_integer(1534236469))
