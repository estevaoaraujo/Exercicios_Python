'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

def valida_nome (nome):
    while True:
        if len(nome)>3:
            return nome
        else:
            print('Nome insuficiente')
            nome = input('Nome: ')

def valida_idade(idade):
    while True:
        if idade > 0 or idade <= 150:
            return idade
        else:
            print('idade incorreta')


def ver (nome):
    print(nome)

def rendimentos(salario):
    while True:
        if salario > 0:
            return salario
        else:
            print('incorreto')
            salario = input('Salario: ')

def persona(sexo):
    while True:
        if sexo == 'f' or sexo == 'F':
            femea = 'Feminino'
            return femea
        elif sexo =='M' or sexo == 'm':
            macho = 'Masculino'
            return macho
        else:
            print('incorreto')
            sexo = input('Sexo: ')


nome = input('Nome: ')
idade = int(input('Idade: '))
salario  = float(input('Salario: '))
sexo = input('Sexo: ')

ver(valida_nome(nome))
ver(valida_idade(idade))
ver(rendimentos(salario))
ver(persona(sexo))


