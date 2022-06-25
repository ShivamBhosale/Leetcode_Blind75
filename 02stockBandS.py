## Stock Buy and Sell
## Category: Array
## Find local min and search for local maximum sliding window.
def maxProfit(prices):
    l,r = 0,1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
        else:
            l = r
        r += 1
    return maxP

print(maxProfit([7,1,5,3,6,4])) 

def maxProfit2(prices2):
    l,r = 0,0
    maxP = 0
    while r < len(prices2):
        if prices2[l] < prices2[r]:
            profit = prices2[r] - prices2[l]
            maxP = max(maxP,profit)
        else:
            l = r
        r += 1
    return maxP

print(maxProfit2([7,1,5,3,6,4])) 