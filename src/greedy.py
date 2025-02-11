def find_coins_greedy(amount: int, coins=[50, 25, 10, 5, 2, 1]) -> dict:
    """
    Жадібний алгоритм для видачі решти.
    
    :param amount: Сума решти, яку потрібно видати.
    :param coins: Список доступних номіналів монет (за замовчуванням відсортовані за спаданням).
    :return: Словник з кількістю монет кожного номіналу.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
        if amount == 0:
            break
    return result
