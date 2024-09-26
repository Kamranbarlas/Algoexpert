def nonConstructibleChange(coins):
    coins.sort()
    min_c = 0
    print(coins)
    for coin in coins:
        print("coin ==> ", coin)
        if coin > min_c + 1:
            return min_c + 1
        min_c += coin
    return min_c + 1