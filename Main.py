def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print('')


def main():
    n = int(input("Введите число n: "))
    multiplication_table(n)

main()

# выбрана процедурная парадигма, т.к. проста и удобна