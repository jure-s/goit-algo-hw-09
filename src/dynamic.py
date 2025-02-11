def find_min_coins(amount: int, coins=[50, 25, 10, 5, 2, 1]) -> dict:
    """
    Алгоритм динамічного програмування для мінімальної кількості монет.
    
    :param amount: Сума решти, яку потрібно видати.
    :param coins: Список доступних номіналів монет.
    :return: Словник з кількістю монет кожного номіналу.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                coin_used[j] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
