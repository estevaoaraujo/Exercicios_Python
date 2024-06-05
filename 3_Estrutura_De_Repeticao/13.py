'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''

base = int(input("Base: "))
expoente = int(input("expoente: "))

resultado = base ** expoente

print(base," elevado ", expoente," = ", resultado)

print("Fazendo loop")

contador = 0
while contador <= expoente:
    resultado = base ** contador
    print(base," elevado ", contador," = ", resultado)
    contador +=1
