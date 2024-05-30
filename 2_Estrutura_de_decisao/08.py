'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

# Possibilidade 1
'''def menu():
    print('1- Produto A ')
    print('2- Produto B ')
    print('3- Produto C ')
    dados = [80.0, 90.00, 120.00]
    return dados

def pergunta(produto,dados):
    if produto == 1:
        print("Produto A = R$ ",dados[0])
    elif produto  == 2:
        print("Produto B = R$ ", dados[1])
    elif produto  == 2:
        print("Produto C = R$ ", dados[2])

def escolha():
    produto = int(input("Escolha: "))    
    return produto

dados = menu()
produto = escolha()
pergunta(produto,dados)'''

# Possibilidade 2

def inserir_preco():
    p1 = float(input("Produto A: "))
    p2 = float(input("Produto B: "))
    p3 = float(input("Produto C: "))
    return p1,p2,p3

def valida(p1,p2,p3):

    if p1 >= p2 and p1 >= p3:
        maior = p1
    elif p2 >= p1 and p2 >= p3:
        maior = p2
    elif p3 >= p1 and p3 >=p2:
        maior = p3

    if p1 <= p2 and p1 <= p3:
        menor = p1
    elif p2 <= p1 and p2 <= p3:
        menor = p2
    elif p3 <= p1 and p3 <=p2:
        menor = p3

    return maior , menor

def resultado(maior,menor):
    print("Maior é ",maior," Menor é ",menor)

p1,p2,p3 = inserir_preco()    
maior, menor = valida(p1,p2,p3)
resultado(maior,menor)