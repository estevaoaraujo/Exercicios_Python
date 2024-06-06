'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

contador = 3
maior = 0
menor = 0
soma = 0

while contador > 0:
    numeros = int(input("Numeros: "))
    soma += numeros

    if numeros > maior:
        maior = numeros
        
    else:
        menor = numeros
        
    contador -=1   

print("Maior valor: ",maior)     
print("Menor valor: ",menor)  
print("Soma total: ", soma) 