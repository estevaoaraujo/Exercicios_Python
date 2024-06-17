#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

n=0
vetor = []

while  n < 5:
    numero = int(input("Numero: "))
    vetor.append(numero)
    n+=1

print(vetor)
