'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Certifica-se de que n1 é o menor e n2 é o maior
if n1 > n2:
    n1, n2 = n2, n1  # Troca os valores se n1 for maior que n2


for num in range(n1 + 1, n2):
    print(num, end=" ")

print("\n")

while n1 < n2-1:
    print(n1+1,end=" ")
    n1+=1