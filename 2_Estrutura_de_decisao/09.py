'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

#Metodo 1 

n1 = int(input("n1: "))
n2 = int(input("n1: "))
n3 = int(input("n1: "))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

if (n1 != maior and n1 != menor):
    meio = n1
elif (n2 != maior and n2 != menor):
    meio = n2
else:
    meio = n3

print(maior,meio,menor)