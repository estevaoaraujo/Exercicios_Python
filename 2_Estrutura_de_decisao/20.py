'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

def leitura():
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    nota3 = float(input("Nota3: "))
    media = (nota1+nota2+nota3)/3
    return round(media,1),nota1,nota2,nota3

def validacao(media):
    if media < 7:
        print("REPROVADO media: ", media)
    elif media >=7 :
        print("APROVADO media: ", media)
    elif media == 10:
        print("APROVADO COM DESTINÇÃO media: ", media)

def menu():
    nome = input("Olá, qual é o seu nome: ")
    print("Prazer,",nome, "Insira as 3 notas")
    media,nota1,nota2,nota3 = leitura()
    validacao(media)

menu()