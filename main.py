import os
from src.greedy import find_coins_greedy
from src.dynamic import find_min_coins

def run_benchmark():
    """Запускає тест продуктивності алгоритмів."""
    os.system("python benchmarks/benchmark.py")

def main():
    while True:
        print("\nСистема видачі решти")
        print("1 - Ввести суму та отримати розрахунок")
        print("2 - Запустити тест продуктивності (Benchmark)")
        print("0 - Вийти")
        
        choice = input("Ваш вибір: ")

        if choice == "0":
            print("Завершення роботи.")
            break
        elif choice == "1":
            try:
                amount = int(input("Введіть суму для видачі решти (або 0 для виходу в меню): "))
                if amount == 0:
                    continue
                if amount < 0:
                    print("Сума має бути додатною.")
                    continue

                print("\nРезультат (Жадібний алгоритм):")
                greedy_result = find_coins_greedy(amount)
                for coin, count in sorted(greedy_result.items(), reverse=True):
                    print(f"Монета {coin} коп.: {count} шт.")

                print("\nРезультат (Динамічне програмування):")
                dp_result = find_min_coins(amount)
                for coin, count in sorted(dp_result.items(), reverse=True):
                    print(f"Монета {coin} коп.: {count} шт.")

            except ValueError:
                print("Помилка: введіть ціле число.")
        elif choice == "2":
            run_benchmark()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
