'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

contador = 1
par = 0
impar = 0

while contador <= 10:
    numero = int(input(f'{contador} -Entrada: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1    
    contador +=1

print(f'Par são {par} impar são {impar}')        