#Faça um Programa que leia três números e mostre o maior deles.

def valida(a,b,c):
    if a > b :
        print(f'Esse é maior valor a  {a}')
    elif b > c:
        print(f'Esse e maior valor b  {b}')      
    elif c > a:
        print(f'Esse é maior valor c {c}')
        
valida(18,10,9)            