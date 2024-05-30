'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

def menu():
    print("1 - Domingo")
    print("2 - Segunda")
    print("3 - Terça")
    print("4 - Quarta")
    print("5 - Quinta")
    print("6 - Sexta")
    print("7 - Sabado")

def leitura():
    escolha = int(input("Escolha: "))  
    return escolha 
 
def decisao(escolha):
    dia = ["Incorreto","Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
    if escolha <=7 and escolha >=0:
        print(dia[escolha])
    else:
        print("Incorreto")

menu()
escolha = leitura()
decisao(escolha)