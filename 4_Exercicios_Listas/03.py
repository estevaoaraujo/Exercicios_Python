#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
n=1
vetor = []

while n <= 4:
    numero = int(input(f'N{n}: '))
    vetor.append(numero)
    soma = sum(vetor)
    resultado = soma / 4
    n+=1

print(resultado)