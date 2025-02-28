#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
inverte_idade = []
inverte_altura = []
n = 5
for i in range(n):
    id = int(input(f'{i+1}ª Idade: '))
    idade.append(id)
    al = float(input(f'{i+1}ª Altura: '))
    altura.append(al)

for i in range(n):
    print(f'Lançamento {i+1} idade é {idade[i]}, altura é {altura[i]}') 

index = 4
while index >= 0:
    inverte_idade.append(idade[index])
    inverte_altura.append(altura[index])
    index -= 1

for i in range(n):
    print(f'Lançamento {i+1} idade é {inverte_idade[i]} altura é {inverte_altura[i]}')


'''inverte_idade = idade[::-1]
inverte_altura = altura[::-1]'''

