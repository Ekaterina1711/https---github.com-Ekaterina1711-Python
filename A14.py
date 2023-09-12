#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#50 -> 1, 2, 4, 8, 16, 32

def print_powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power = power << 1

N = int(input("Введите число N: "))
print("Целые степени двойки, не превосходящие число N:")
print_powers_of_two(N)