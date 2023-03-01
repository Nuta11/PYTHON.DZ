# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

a = int(input("Введите число: "))
b = int(input("В какую степень возвести число: "))

def exponentiation(a1, b):
    if b == 1:
        return a1
    return exponentiation(a1 * a, b - 1)

print(f'Число {a} в степени {b} равно {exponentiation(a, b)}.')