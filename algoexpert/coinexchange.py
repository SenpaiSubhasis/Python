def coin(n,denoms):
    ways = [1]+[0]*n
    for denom in denoms:
        for amount in range(1,n+1):
            if denom<=amount:
                ways[amount] = ways[amount]+ways[amount-denom]
    
    return ways[n]

x = coin(10,[1,5,10,25])
print(x)