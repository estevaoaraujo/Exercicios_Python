#Faça um programa que leia 5 números e informe o maior número.

contador = 0
maior = 0

while contador < 5:
    numero = int(input("Numeros:  "))
    if maior < numero:
        maior = numero
    contador +=1    
    
print(maior)