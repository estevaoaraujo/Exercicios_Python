'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''
#Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
resultado = 0

while numero1 != numero2:
    if numero1 > numero2:
        numero2 += 1
        resultado = resultado + numero2
        print(numero2)
    else:
        numero1 < numero2    
        numero1 += 1
        resultado = resultado + numero1
        print(numero1)                             
print("Soma: ",resultado)