#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def valida(n):
    if n > 0:
        return n
    else:
        print(f'Numero negativo {n}')
        return ''
        
numero = int(input('numero:'))
print(valida(numero))


