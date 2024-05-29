'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

def calcula_homens(altura):
    return (72.7*altura) - 58

def calcula_mulher(altura):
    return (62.1*altura) - 44.7

alt = float(input("DIgite altura: "))
calcula_homens(alt)
calcula_mulher(alt)

print("O peso ideal para a altura se for homem é ", alt, "metros é:", round(calcula_homens(alt),2), "quilogramas\n")
print("O peso ideal para a altura se for mulher é ", alt, "metros é:", round(calcula_mulher(alt),2), "quilogramas\n")