'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

def dobro_primeiro(valor1,valor2):
    return (valor1 * 2) + (valor2 / 2)

def inserir():
    val1 = int(input("Digite valor1: "))
    val2 = int(input("DIgite valor2: "))
    val3 = float(input("Digite valor3: "))
    return val1,val2,val3

def soma_triplo(valor1,valor2,valor3):
    return (valor1 * 3) + valor3

def cubo(valor3):
    return val3 ** 3

val1,val2,val3 = inserir()
print(dobro_primeiro(val1,val2))
print(soma_triplo(val1,val2,val3))
print(cubo(val3))
