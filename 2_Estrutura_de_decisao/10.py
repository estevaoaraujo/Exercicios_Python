'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

def menu():
    print("M-matutino \nV-Vespertino \nN- Noturno")

def decisao():
    escolha = input("Escolha: ")

    if escolha == 'M' or escolha == 'm':
        print("Bom dia!!!")  
    elif escolha == 'V' or escolha == 'v':
        print("Boa tarde") 
    elif escolha == 'N' or escolha == 'n':
        print("Boa noite!!!")     
    else:
        print('Botão invalido')       

menu()
decisao()