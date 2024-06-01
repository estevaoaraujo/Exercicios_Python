'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

numero = 0
contador = 0

while contador < 5:
    valor = int(input("Numero: "))
    numero += valor
    contador +=1

total = numero / 5
print(total)