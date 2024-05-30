'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

def leitura(x,y):
    nota = (x+y)/2
    return nota

def verifica(valor):
    if valor >=7 and valor < 9.9:
        print(f'Aprovado com {valor}')
    elif valor < 7:
        print(f'Reprovado com {valor}')
    elif valor == 10:
        print(f'Voce e monstruoso com {valor}')

nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))  
valor = leitura(nota1,nota2)
verifica(valor)
