'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

def leitura():
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    return lado1, lado2, lado3

def eh_triangulo(l1, l2, l3):
    return (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)

def tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    l1, l2, l3 = leitura()
    
    if eh_triangulo(l1, l2, l3):
        tipo = tipo_triangulo(l1, l2, l3)
        print(f"Os lados fornecidos formam um triângulo {tipo}.")
    else:
        print("Os lados fornecidos não podem formar um triângulo.")

if __name__ == "__main__":
    main()
