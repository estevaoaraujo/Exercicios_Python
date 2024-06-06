'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

  5 * 1 = 5
  5 * 4 = 20
 20 * 3 = 60
 60 * 2 = 120
120 * 1 = 120

'''

numero = int(input("Número: "))
resultado = 1
fator = numero

while numero > 0:
    if numero !=0:
        resultado *=numero
    numero -=1

print(fator,"! = ",resultado)

# ou 


def fatorial(n):
    
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado


numero = int(input("Digite um número inteiro: "))


resultado_fatorial = fatorial(numero)


print(f"{numero}! = {resultado_fatorial}")