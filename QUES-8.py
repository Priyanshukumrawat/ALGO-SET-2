def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')  
    max_profit = 0             

    for price in prices:
        if price < min_price:
            min_price = price
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", max_profit(prices))