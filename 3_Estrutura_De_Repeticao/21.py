'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro: "))

# Verifica se o número é primo
if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")



