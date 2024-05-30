'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
  se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

def menu():
    print("Entre 9.0 e 10.0        A\nEntre 7.5 e 9.0         B\nEntre 6.0 e 7.5         C\nEntre 4.0 e 6.0         D\nEntre 4.0 e zero        E")

def leitura():
    nota1 = float(input("NOTA 1: "))
    nota2 = float(input("NOTA 2: "))
    media = (nota1 + nota2) /2
    return round (media,2)

def processamento(media):
    if media >= 0 and media <=4.0:
        print(f'conceito E NOTA={media} Reprovado')
    elif media >=4.1 and media <= 6.0:
        print(f'conceito D NOTA={media} Reprovado')
    elif media >= 6.1 and media <= 7.5:
        print(f'conceito C NOTA={media} Aprovado')
    elif media >= 7.6 and media <= 9.0:
        print(f'conceito B NOTA= {media} Aprovado')
    elif media >= 9.1 and media <= 10.0:
        print(f'conceito A NOTA= {media} Aprovado')

menu()
media = leitura()
processamento(media)
