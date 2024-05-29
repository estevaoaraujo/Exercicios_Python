'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
 usando a seguinte fórmula: (72.7*altura) - 58'''

def calcula(altura):
    return (72.7*altura) - 58


alt = float(input(" Altura: "))

result = (round(calcula(alt),2))
print("O peso ideal para a altura", alt, "metros é:", result, "quilogramas")


