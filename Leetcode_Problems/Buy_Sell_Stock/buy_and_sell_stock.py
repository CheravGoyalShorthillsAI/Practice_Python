from typing import List

def max_profit(prices: List[int]) -> int:
    # Initialize variables to store the minimum price and the maximum profit
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price if a lower price is found
        if price < min_price:
            min_price = price
        # Calculate the profit by subtracting the minimum price from the current price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
