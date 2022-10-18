# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# OMG Way
# def maxProfit(prices):
#     profit = 0
#     low, high = prices[0], 0
#
#     for i in range(1, len(prices)):
#         if prices[i] < high:
#             profit += high - low
#             low = prices[i]
#             high = 0
#
#         if prices[i] < low:
#             low = prices[i]
#         else:
#             high = prices[i]
#
#             if i == len(prices) - 1:
#                 if high > low: profit += high - low
#     return profit if profit != 0 else high - low if high > low else 0


# List comprehension
def maxProfit(prices):
    return sum(prices[i]-prices[i-1] if prices[i] > prices[i-1] else 0 for i in range(1, len(prices)))


print(maxProfit([7, 1, 5, 3, 6, 4]))  # Should return 7
print(maxProfit([1, 2, 3, 4, 5]))  # Should return 4
print(maxProfit([6, 1, 3, 2, 4, 7]))  # Should return 7
