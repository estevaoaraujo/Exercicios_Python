'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

def menu():
    nome = input("Olá, sou policial x, qual é seu nome: ")
    pergunta = input(f"Prazer {nome}, vou te fazer algumas perguntas?")
    print(" Digite sim ou não")
    entrevista(nome)

def entrevista(nome):
    p1 = input(f"{nome},Telefonou para a vítima? ")
    p2 = input("Esteve no local do crime? ")
    p3 = input("Mora perto da vítima? ")
    p4 = input("Devia para a vítima? ")
    p5 = input("Já trabalhou com a vítima? " )
    analisa(p1,p2,p3,p4,p5,nome)

def analisa(p1,p2,p3,p4,p5,nome):
    nivel = 0
    if p1 == "sim":
        nivel += 1
    if p2 == "sim":
        nivel += 1    
    if p3 == "sim":
        nivel += 1
    if p4 == "sim":
        nivel += 1
    if p5 == "sim":
        nivel += 1
    
    valida(nivel, nome) 

def valida(nivel,nome):
    if nivel == 0 or nivel == 1:
        print(nome, "Obrigado por seu tempo, inicente")
    if nivel == 2:
        print(nome," voce me parrece meio suspeito! ")
    if nivel == 3 or nivel == 4:
        print(nome ," voce me parrece cumplice! ")   
    if nivel == 5:
        print(nome," vamos para delegacia voce esta preso, voce e assasino! ")         
menu()