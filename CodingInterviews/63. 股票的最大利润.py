def maxProfit(prices: list) -> int:
    maxPro = 0
    minPri = None
    for price in prices:
        if price < minPri if minPri is not None else True:
            minPri = price
        maxPro = max(maxPro, price - minPri)
    return maxPro

