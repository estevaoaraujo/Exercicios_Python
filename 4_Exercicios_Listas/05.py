#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor =[]
consoantes = 0
i = 1

while i <= 10:
    n = input(f'{i} Caracteres: ')
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        pass
    else:
        consoantes += 1
        vetor.append(n)
    i+=1

print('São ', consoantes,'consoantes no Vetor de ',vetor)

#ou 


# O método .lower() é usado para tratar os caracteres de forma case-insensitive, ou seja, tanto 'A' quanto 'a' serão considerados.
# 'n.isalpha() garante que o caractere é uma letra.
# 'n not in 'aeiou' é uma maneira mais clara e eficiente de verificar se o caractere é uma consoante.
vetor = []
consoantes = 0
i = 0

while i < 10:
    n = input(f'{i+1}º Caracter: ').lower()
    if n.isalpha() and n not in 'aeiou':
        consoantes += 1
        vetor.append(n)
    i += 1

print(f'São {consoantes} consoantes no vetor: {vetor}')
