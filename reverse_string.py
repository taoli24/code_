def reverse_string(s):
    l, r = 0, len(s) - 1
    for i in range(len(s) // 2):
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


print(reverse_string(["H", "a", "n", "n", "a", "h"]))
