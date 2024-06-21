#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# Inicializar um vetor vazio
vetor = []

# Ler 10 números reais e adicioná-los ao vetor
for i in range(10):
    numero = float(input("Digite um número real: "))
    vetor.append(numero)

# Mostrar os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(vetor):
    print(numero)

