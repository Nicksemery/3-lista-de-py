# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

num = int(input("qual tabuada você que saber? "))
cal = range(1,11)
for tab in cal:
    print (tab * num)