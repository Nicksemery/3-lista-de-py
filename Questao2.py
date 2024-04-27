# Faça um programa que mostre as tabuadas dos números de 1 a 10.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for tab in numeros:
    print(f"de {tab}: ")
    for mul in numeros:
        print(tab*mul)
