'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

def menu():
    print(" Escolha operedores digitando: 0 , 1 , 2 , 3 ")
    print("0 - Soma")
    print("1 - Subtração'")
    print("2 - Divisão\n")
    print("3 - Multiplicão\n")

def leitura():
    n1 = float(input("Número1: "))
    n2 = float(input("Número2: "))
    operador = input("Operador: ")
    return n1,n2,operador

def calculadora(n1,n2,operador):
    if operador == '0':
        result = n1 + n2
        valida(result)
    if operador == '1':
        result = n1 - n2
        valida(result)
    if operador == '2':
        result = n1 / n2
        valida(result)
    if operador == '3':
        result = n1 * n2
        valida(result)

def valida(result):
    print("Valor: ",result)
    if result % 2 == 0:
        print("E par")  
    else:
        print("E impar")          

    if result < 0:
        print("Negativo")
    else:
        print("Positivo")    

    if result == int(result):
        print("Inteiro")
    else:
        print("Decimal")    

menu()
n1,n2,operador = leitura()        
calculadora(n1,n2,operador)