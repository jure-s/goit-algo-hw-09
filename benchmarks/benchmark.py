import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.greedy import find_coins_greedy
from src.dynamic import find_min_coins

def benchmark(amount):
    print(f"\nТест продуктивності для суми: {amount} коп.")

    # Вимірюємо час виконання жадібного алгоритму
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Вимірюємо час виконання алгоритму динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    # Виводимо результати
    print(f"Жадібний алгоритм: {greedy_time:.6f} сек.")
    print(f"Динамічне програмування: {dp_time:.6f} сек.")

if __name__ == "__main__":
    for amount in [1000, 5000, 10000, 50000, 100000]:  # Тестуємо на різних сумах
        benchmark(amount)
