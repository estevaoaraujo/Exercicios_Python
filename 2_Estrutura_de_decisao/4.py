#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a','e','i','o','u','A','E','I','O','U']

entrada = input('Letra: ')

if entrada in vogais:
    print(f'E vogal  {entrada}')
else:
    print('Nao e vogal')


#ou 

def verificar_letra(letra):
    vogais = 'aeiouAEIOU'
    
    if letra.isalpha() and len(letra) == 1:
        if letra in vogais:
            print(f'A letra "{letra}" é uma vogal.')
        else:
            print(f'A letra "{letra}" é uma consoante.')
    else:
        print('Por favor, digite apenas uma letra do alfabeto.')


letra = input("Digite uma letra: ")
verificar_letra(letra)
