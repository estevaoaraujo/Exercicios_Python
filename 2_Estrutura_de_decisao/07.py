def ler():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))
    return num1, num2, num3

def valida(num1, num2, num3):
    # Encontrando o maior número
    if num1 >= num2 and num1 >= num3:
        maior = num1
    elif num2 >= num1 and num2 >= num3:
        maior = num2
    else:
        maior = num3
    
    # Encontrando o menor número
    if num1 <= num2 and num1 <= num3:
        menor = num1
    elif num2 <= num1 and num2 <= num3:
        menor = num2
    else:
        menor = num3
    
    print("Maior número:", maior)
    print("Menor número:", menor)

num1, num2, num3 = ler()
valida(num1, num2, num3)

#ou 

def main():
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    # Encontrando o maior número
    maior = max(num1, num2, num3)
    
    # Encontrando o menor número
    menor = min(num1, num2, num3)
    
    # Exibindo os resultados
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

if __name__ == "__main__":
    main()
