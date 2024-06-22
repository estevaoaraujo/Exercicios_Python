#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []
produto = 1  # Inicializa o produto com 1

# Leitura dos números e armazenamento no vetor
for i in range(5):
    n = int(input(f'{i+1}º Número: '))
    vetor.append(n)
    produto *= n  # Multiplica cada número ao calcular o produto

# Mostra a soma dos números
print(f'Soma dos números: {sum(vetor)}')

# Mostra o produto dos números
print(f'Produto dos números: {produto}')

# Mostra os números do vetor
print(f'Números no vetor: {vetor}')
  