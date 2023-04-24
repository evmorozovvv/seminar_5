#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def stepen(x, y):
    if y == 1:
        return x
    return x*stepen(x, y-1)

a = int(input("Введите число "))
b = int(input("Введите степень "))

print(stepen(a, b))


