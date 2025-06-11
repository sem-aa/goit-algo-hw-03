def hanoi(n, from_, to, via, state):
    if n == 1:
        disk = state[from_].pop()
        state[to].append(disk)
        print(f"Перемістити диск з {from_} на {to}: {disk}")
        print("Проміжний стан:", state)
        return

    hanoi(n - 1, from_, via, to, state)
    hanoi(1, from_, to, via, state)
    hanoi(n - 1, via, to, from_, state)


def main():
    try:
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            raise ValueError("Кількість має бути більше нуля.")
    except ValueError as e:
        print("Помилка:", e)
        return

    state = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
        'B': [],
        'C': []
    }

    print("Початковий стан:", state)
    hanoi(n, 'A', 'C', 'B', state)
    print("Кінцевий стан:", state)


if __name__ == "__main__":
    main()
