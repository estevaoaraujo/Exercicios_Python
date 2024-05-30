import math

def leitura_coeficientes():
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    return a, b, c

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        x1 = -b / (2*a)
        return x1, None
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

def main():
    print("Resolvendo a equação do segundo grau na forma ax² + bx + c = 0")
    a, b, c = leitura_coeficientes()
    
    if a == 0:
        print("O coeficiente 'a' não pode ser zero em uma equação do segundo grau.")
        return
    
    x1, x2 = calcular_raizes(a, b, c)
    
    if x1 is None and x2 is None:
        print("A equação não possui raízes reais.")
    elif x2 is None:
        print(f"A equação possui uma raiz real: x = {x1}")
    else:
        print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")

if __name__ == "__main__":
    main()

