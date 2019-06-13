'''
LeetCode 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    minimum = prices[0]
    tmp = 0
    ans = 0
    for i in prices[1:]:
        if minimum > i:
            minimum = i
        else:
            tmp = i - minimum
            if tmp > ans:
                ans = tmp
    return ans