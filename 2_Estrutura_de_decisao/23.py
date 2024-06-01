'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

def verifica_numero(numero):
    if numero == int(numero):
        return "inteiro"
    else:
        return "decimal"

numero = float(input("Digite um número: "))
tipo = verifica_numero(numero)
print(f"O número {numero} é {tipo}.")
